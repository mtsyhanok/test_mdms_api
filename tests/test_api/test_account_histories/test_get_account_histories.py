import json
from pkg_resources import resource_string

import jsonschema
from hamcrest import assert_that, equal_to, has_entries, has_item

from libs.api.common import generate_string
from settings import ERROR_MESSAGES, SALES_PLAN_AFF


def test_get_account_histories_json_schema(abo_with_history, authorized_user):
    """
    Test checks that response of GET '/accounts/{salesPlanAff}-{aboNum}/histories' corresponds to expected json schema
    """
    response = authorized_user.get_account_histories(abo=abo_with_history['id'], expected_status_code=200)
    expected_json_schema = json.loads(resource_string(__name__, '/expected_schema.json'))
    jsonschema.validate(response, expected_json_schema)


def test_get_account_histories_data(abo_with_history, authorized_user):
    """
    Test checks that response of GET '/accounts/{salesPlanAff}-{aboNum}/histories'
    contains proper history data of the Abo
    """
    response = authorized_user.get_account_histories(abo=abo_with_history['id'], expected_status_code=200)
    # Note: values below are hardcoded to illustrate how has_entries matcher works.
    # In real test values to compare will be taken from abo_with_history's data
    assert_that(response, has_item(has_entries(actionCd='Block/Privilege Delete',
                                               countryCd='US',
                                               processTypeCd='Rights Management - Blocks and Prvileges',
                                               processDate='2019-10-19T06:31:41-04:00',
                                               aboNum=abo_with_history['id'],
                                               salesPlanaff=SALES_PLAN_AFF)))


def test_get_account_histories_nonexistent_abo(authorized_user):
    """
    Test checks that response of GET /accounts/{salesPlanAff}-{aboNum}/histories'
    returns 404 error for nonexistent {aboNum}
    """
    abo_num = generate_string(5, digits_only=True)
    response = authorized_user.get_account_histories(abo=abo_num, expected_status_code=404, return_json=False)
    assert_that(response.text, equal_to(ERROR_MESSAGES[404]))


def test_get_account_histories_missed_abo_num(authorized_user):
    """
    Test checks that response of GET /accounts/{salesPlanAff}-/histories' returns 400 error
    """
    response = authorized_user.get_account_histories(abo=None, expected_status_code=400, return_json=False)
    assert_that(response.text, equal_to(ERROR_MESSAGES[400]))


def test_get_account_histories_unauthorized(abo_with_history, unauthorized_user):
    """
    Test checks that unauthorized user doesn't have access to GET /accounts/{salesPlanAff}-{aboNum}/histories'
    """
    response = unauthorized_user.get_account_histories(abo=abo_with_history['id'], expected_status_code=401,
                                                       return_json=False)
    assert_that(response.text, equal_to(ERROR_MESSAGES[401]))
