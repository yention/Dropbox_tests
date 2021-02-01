class TestData():

    ACCOUNT_DATES = {
        "email": "downs2811@gmail.com",
        "password": "TEST123pass"
    }


    MAIN_PAGE = {
        'url': 'https://www.dropbox.com/',
        'title': 'Dropbox'
    }

    LOGIN_PAGE = {
        'url': MAIN_PAGE['url'] + 'login',
        'title': 'Login - Dropbox'
    }

    PLANS_PAGE = {
        'url': MAIN_PAGE['url'] + 'plans',
        'title': 'Compare All Dropbox Plans ‐ Dropbox'
    }

    PagesCollection = [MAIN_PAGE, LOGIN_PAGE]


    CUSTOMER_STORIES = {
        'url': MAIN_PAGE['url'] + 'business/customers',
        'title': 'Customers - Dropbox Business'
    }

    HOW_WE_INTEGRATE = {
        'url': MAIN_PAGE['url'] + 'app-integrations',
        'title': 'App Integrations - Dropbox'
    }

    SMART_WORKPLACE = {
        'url': MAIN_PAGE['url'] + 'smart-workspace',
        'title': 'Smart Workspace for the Modern Workday - Dropbox'
    }


    DO_MORE_THAN_STORE = {
        'url': 'https://experience.dropbox.com/',
        'title': "Experience - Dropbox"
    }

    DROPDOWN_WHY_DROPBOX = [CUSTOMER_STORIES, HOW_WE_INTEGRATE, SMART_WORKPLACE, DO_MORE_THAN_STORE]



