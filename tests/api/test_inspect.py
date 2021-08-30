"""
to be updated
"""
from api.inspect import InspectAPI


def test_inspect(test_info, host_name, project_id, api_key):
    """
    test function for inspect
    :param test_info:
    :param host_name:
    :param project_id:
    :param api_key:
    :return:
    """
    inspect_api = InspectAPI(host_name, project_id, api_key)
    inspect_api.inspect_text_content("Credit Card Type Credit Card Number American Express 3714-2963-5398-431 Diners "
                                     "Club 3056-9309-224904 Discover 6011-1111-1115-1117 JCB 3530111633300000 "
                                     "MasterCard 5555555565554444 Visa 4111111121111111")
    print(test_info)
    assert True
