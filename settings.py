import os

AFFILIATES = {
    'Scandinavia': {'id': '460', 'host': ''},
    'ANA': {'id': '010', 'host': 'http://dms-service-qa:8080/DMS_Service_Web/api/v3'},
    'Thailand': {'id': '200', 'host': ''},
    'Indonesia': {'id': '220', 'host': ''},
    'Korea': {'id': '180', 'host': ''}
}

AFFILIATE_TO_TEST = os.getenv('SALES_PLAN_AFF', 'ANA')
SALES_PLAN_AFF = AFFILIATES[AFFILIATE_TO_TEST]['id']
MDMS_HOST = AFFILIATES[AFFILIATE_TO_TEST]['host']

ERROR_MESSAGES = {
    400: 'Bad Request',
    401: 'Unauthorized',
    404: 'Not Found'
}


###############################
# Web tests settings

# PATH to chromedriver
WEBDRIVER_PATH = ""

HEALTH_BRIDGE_HOST = 'https://myhealthbridge.com'
