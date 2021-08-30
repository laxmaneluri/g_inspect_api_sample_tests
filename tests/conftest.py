"""
To be updated
"""
import logging
import os

import pytest
import sys
from os.path import dirname as d
from os.path import abspath, join

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
root_dir = d(d(abspath(__file__)))
LOGGER.debug("****** >>>>>>%s", root_dir)
sys.path.append(root_dir)

tests = [
    {
        'a': 1
    },
    {
        'b': 2
    },
    {
        'c': 3
    },
    {
        'd': 4
    },
]


@pytest.fixture
def host_name(variables):
    """
    reading the host_name from config json
    :param variables: config json object
    :return:
    """
    LOGGER.debug("host name::: %s", variables.get("host_name"))
    return variables.get("host_name")


@pytest.fixture
def project_id(variables):
    """
    reading the project_id from config json
    :param variables: config json object
    :return:
    """
    LOGGER.debug("project_id::: %s", variables.get("project_id"))
    return variables.get("project_id")


@pytest.fixture
def api_key(variables):
    """
    reading the api key from config json
    :param variables: config json object
    :return:
    """
    LOGGER.debug("api_key::: %s", variables.get("api_key"))
    return variables.get("api_key")


def pytest_generate_tests(metafunc):
    """

    :param metafunc: test function
    :return:
    """
    metafunc.parametrize("test_info", tests)
