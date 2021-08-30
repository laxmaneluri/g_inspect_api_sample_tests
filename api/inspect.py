"""
to be updated
"""
import logging

from urllib.parse import urljoin
from common.restclient import RestClient

LOGGER = logging.getLogger(__name__)
END_POINT = "v2/projects/{}/content:inspect"
QUERY_PARAM = "key={}"
BASE_URL = "https://{}"


class InspectAPI(RestClient):
    """
    To be updated
    """
    response = None
    json_object = {}

    def __init__(self, hostname, project_id, api_key):
        self.url = urljoin(BASE_URL.format(hostname), END_POINT.format(project_id) + "?key={}".format(api_key))
        LOGGER.debug("url::: %s", self.url)
        super().__init__(self.url)

    def inspect_text_content(self, text, config_obj=None):
        """
        function to call inspect api
        :param text: text for inspection
        :param config_obj: config_object
        :return:
        """
        json_body = self.get_json_body(text, config_obj)
        self.response = self.post(json_body)
        LOGGER.debug(self.response)

    def get_json_body(self, text, config_obj):
        """
        function to form json body for inspect request
        :param text: text if item used is text
        :param config_obj: config_obj for inspect configuration
        :return:
        """
        self.json_object = {}

        if text:
            item = {
                "item": {
                    "value": text
                }
            }
            self.json_object.update(item)
        if config_obj:
            self.json_object.update(config_obj)
        LOGGER.debug("json_body:::%s", self.json_object)
        return self.json_object
