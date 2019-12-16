import allure
import requests

from libs.api.common import allure_attach_json, allure_attach_plain_text
from settings import MDMS_HOST, SALES_PLAN_AFF


class UnexpectedStatusCode(requests.RequestException):
    pass


class BaseApiSteps(object):

    def __init__(self):
        self.base_url = MDMS_HOST
        self._session = requests.Session()
        self.timeout = 10

    @property
    def session(self):
        return self._session

    @allure.step('Preform request {method} {url}')
    def call(self, method, url, data=None, expected_status_code=None, return_json=True, abo=None):
        url = self.base_url + url
        if abo:
            self.session.headers.update({'aboNum': str(abo)})
        req = requests.Request(method, url, data=data)
        prepared_request = self.session.prepare_request(req)
        response = self.session.send(prepared_request)

        if expected_status_code:
            if response.status_code != expected_status_code:
                err_msg = 'Expected status code {0}, but was {1}'.format(expected_status_code, response.status_code)
                raise UnexpectedStatusCode(err_msg, response=response)

        if return_json:
            allure_attach_json(response.json(), 'result of {0} {1}'.format(method, url))
            return response.json()
        else:
            allure_attach_plain_text(response.text, 'result of {0} {1}'.format(method, url))
            return response


class API(BaseApiSteps):

    def post_abo(self, data=None, expected_status_code=None):
        pass

    def delete_abo(self, abo_id, expected_status_code=None):
        pass

    def get_account_histories(self, abo, expected_status_code=None, **kwargs):
        url = '/accounts/{0}-{1}/histories?pageSize=100&requestingPage=1'.format(SALES_PLAN_AFF, abo)
        return self.call('GET', url, expected_status_code=expected_status_code, abo=abo, **kwargs)
