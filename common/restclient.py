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

    def __init__(self, url, headers=None, verify=None):
        """

        :param url:
        :param headers:
        :param verify:
        :param kwargs:
        """
        self.url = url
        self.headers = headers
        self.verify = verify

    def get(self, json=None, data=None, headers=None):
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


        requests_obj = requests.request("GET", self.url, json=json,data=data, verify=self.verify,
                                            timeout=30)
        return requests_obj

    def post(self, json=None, data=None, headers=None):
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

        requests_obj = requests.request("POST", self.url, json=json, data=data, verify=self.verify,
                                            timeout=30)
        return requests_obj
