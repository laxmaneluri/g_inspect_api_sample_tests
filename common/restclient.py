"""
To be updated
"""
import logging

import requests

LOGGER = logging.getLogger(__name__)

class RestClient():
    """
     to be updated
    """

    def __init__(self, uri, headers=None, verify=None):
        """

        :param uri:
        :param headers:
        :param verify:
        :param kwargs:
        """
        self.uri = uri
        self.headers = headers
        self.verify = verify

    def get(self, endpoint, json=None, data=None, headers=None):
        """

        :param endpoint:
        :param json:
        :param data:
        :param params:
        :param headers:
        :param timeout:
        :return:
        """

        LOGGER.debug("Entered get method")

        if headers:
            headers=self.headers
        url = self.uri + endpoint

        requests_obj = requests.request("GET", url, json=json,data=data, verify=self.verify,
                                            timeout=30)
        return requests_obj

    def post(self, endpoint, json=None, data=None, headers=None):
        """

        :param endpoint:
        :param json:
        :param data:
        :param params:
        :param headers:
        :param timeout:
        :return:
        """

        LOGGER.debug("Entered post method")

        if headers:
            headers = self.headers
        url = self.uri + endpoint

        requests_obj = requests.request("POST", url, json=json, data=data, verify=self.verify,
                                            timeout=30)
        return requests_obj
