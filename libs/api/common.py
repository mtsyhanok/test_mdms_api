import json
import random
import string

import allure


def generate_string(length, digits_only=True):
    if digits_only is True:
        s = string.digits
    else:
        s = string.ascii_letters + string.digits + '.' + '_'
    return ''.join(random.sample(s, length))


def pack_headers_with_authorization(sales_plan_aff):
    headers = {
        'salesPlanAff': str(sales_plan_aff),
        'X-Request-Id': 'b92ad9ea9278414da6575ab0fa7865e',
        'X-Mashery-Oauth-Client-Id': 'DevelopmentTeam{0}ClientId'.format(sales_plan_aff),
        'Authorization': 'Bearer RE1TOmZ2TmQ5c0FI'
    }
    return headers


def allure_attach_json(json_to_attach, message):
    """Publish JSON as attach to allure step"""
    pretty_json = json.dumps(json_to_attach, ensure_ascii=False, indent=4, sort_keys=True)
    allure.attach(name=message, body=pretty_json, attachment_type=allure.attachment_type.JSON)


def allure_attach_plain_text(text_to_attach, message):
    """Publish Text as attach to allure step"""
    allure.attach(name=message, body=text_to_attach, attachment_type=allure.attachment_type.TEXT)


def generate_abo_data():
    # ToDo: generate data to POST Abo
    data = {}
