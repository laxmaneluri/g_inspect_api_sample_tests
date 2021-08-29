"""
to be updated
"""
from common.restclient import RestClient

END_POINT = "v2/projects/{}/content:inspect"
QUERY_PARAM = "key={}"


class InspectAPI(RestClient):
    """
    To be updated
    """
    def __init__(self, base_url, project_id, api_key):
        url = base_url + END_POINT.format(project_id) + "?" +  QUERY_PARAM.format(api_key)
        super().__init__(url)
