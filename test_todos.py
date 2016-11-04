from nose.tools import assert_true, assert_is_not_none, assert_list_equal
import requests
from services import get_todos
from unittest.mock import Mock,patch


# def test_request_response():
#     response = get_todos()
#     assert_true(response.ok)

@patch('services.requests.get')
def test_getting_todos(mock_get):

    todos = [{
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False  }]

    # Configure the mock to return a response with an OK status code.
    #mock_get.return_value.ok = True

    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = todos

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.

    #assert_is_not_none(response)

    assert_list_equal(response.json(), todos)
