"""
to be updated
"""
import logging

from api.inspect import InspectAPI

LOGGER = logging.getLogger(__name__)


def test_inspect(test_info, host_name, project_id, api_key):
    """
    test function for inspect
    :param test_info:
    :param host_name:
    :param project_id:
    :param api_key:
    :return:
    """
    LOGGER.debug(test_info)
    LOGGER.info("test execution stated:::: %s", test_info["test_case_id"])
    inspect_api = InspectAPI(host_name, project_id, api_key)
    inspect_api.inspect_text_content(test_info["test_input_params"]["text"])
    assert inspect_api.validate_findings_count(test_info["expected_output"]["total_findings_count"])
    assert True
