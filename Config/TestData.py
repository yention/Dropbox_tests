class TestData:
    ACCOUNT_DATES = {
        "email": "downs2811@gmail.com",
        "password": "TEST123pass"
    }

    ACCOUNT_INVALID_DATES = {
        "email": ["downs2811@gmail.com", "downs2811gmail.com",  "d0wns2811@gmail.com", "downs2811@gmail.cоm", "downs2811@gmail.org"],
        "password": ["TEST123pass ", " TEST123pass",  "TEST13pass", "TEST123pAss", "TEST123pаss"]
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
        'title': 'Customers - Dropbox Business',
        'name': 'Customer stories'
    }

    HOW_WE_INTEGRATE = {
        'url': MAIN_PAGE['url'] + 'app-integrations',
        'title': 'App Integrations - Dropbox',
        'name': 'How we integrate'
    }

    SMART_WORKPLACE = {
        'url': MAIN_PAGE['url'] + 'smart-workspace',
        'title': 'Smart Workspace for the Modern Workday - Dropbox',
        'name': 'Smart workspace'
    }

    DO_MORE_THAN_STORE = {
        'url': 'https://experience.dropbox.com/',
        'title': "Experience - Dropbox",
        'name': 'Do more than store'
    }

    DROPDOWN_WHY_DROPBOX = [CUSTOMER_STORIES, HOW_WE_INTEGRATE, SMART_WORKPLACE, DO_MORE_THAN_STORE]
