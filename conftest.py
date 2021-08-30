"""

"""


def pytest_addoption(parser):
    """

    :param parser:
    :return:
    """
    parser.addoption("--test_json", action="store", help="Enter the test json file you want to execute."
                                                         "Eg. --test_json=testdata/tests.json", required=True)
