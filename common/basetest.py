"""
To be updated
"""
# pylint: disable=unnecessary-pass

import logging

LOGGER = logging.getLogger(__name__)


class APIBaseTest():
    """
    base test for all rest api tests
    """
    def __init__(self):
        self.response = None

    def assert_response_code(self, response_code):
        """
        placeholder
        :param response_code:
        :return:
        """
        pass

    def assert_response_json(self):
        """
        placeholder
        :return:
        """
        pass
