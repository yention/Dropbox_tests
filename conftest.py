import pytest
import requests
from requests.exceptions import ConnectionError
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

REMOTE_URL = 'http://127.0.0.1:4444/wd/hub'


def is_grid_up():
    try:
        response = requests.get(REMOTE_URL)
    except ConnectionError:
        print('Grid is DOWN!')
        return False

    print('Grid is UP!')
    return response.status_code == 200


def init_remote_driver_chrome():
    if is_grid_up():
        caps = DesiredCapabilities.CHROME.copy()
        driver = webdriver.Remote(command_executor=REMOTE_URL,
                                  desired_capabilities=caps)
    else:
        options = webdriver.ChromeOptions()
        options.headless = False
        options.add_argument("--start-maximized")
        options.add_argument('--reruns 2')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.switch_to.window(driver.window_handles[1])
    return driver


def init_remote_driver_firefox():
    if is_grid_up():
        caps = DesiredCapabilities.FIREFOX.copy()
        driver = webdriver.Remote(command_executor=REMOTE_URL,
                                  desired_capabilities=caps)
    else:
        options = webdriver.FirefoxOptions()
        options.headless = True
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

    return driver


@pytest.fixture(params=['chrome'], scope='class', autouse=True)
def init_driver(request):
    driver = None
    if request.param == 'chrome':
        driver = init_remote_driver_chrome()
    elif request.param == 'firefox':
        driver = init_remote_driver_firefox()
    else:
        print('Please pass the correct browser name: {}'.format(request.param))
        raise Exception('driver is not found')

    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.quit()
