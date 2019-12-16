import allure
from pytest import fixture

from libs.api.api import API
from libs.api.common import pack_headers_with_authorization
from settings import SALES_PLAN_AFF


@fixture(scope='session')
def authorized_user():
    """Fixture returns API object with authorization headers in session"""
    api = API()
    api.session.headers = pack_headers_with_authorization(SALES_PLAN_AFF)
    return api


@fixture(scope='session')
def unauthorized_user():
    """Fixture returns API object without authorization headers in session"""
    return API()


@allure.step('Create Abo with history')
@fixture(scope='module')
def abo_with_history(authorized_user):
    """Fixture creates and returns Abo with history"""
    abo = authorized_user.post_abo()
    # ToDo: create history for Abo
    yield abo

    # delete Abo in the end of the test
    try:
        authorized_user.delete_abo(abo_id=abo['id'])
    except AssertionError:
        print('Abo {} was not found.'.format(abo['id']))
