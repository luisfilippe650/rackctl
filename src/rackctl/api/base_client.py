from requests.exceptions import ConnectionError, Timeout, HTTPError, RequestException, InvalidURL
from rackctl.utils.configuration import BASE_URL, TIMEOUT
from urllib.parse import urlencode
import requests


class ErrorResponse:
    def __init__(self, error: Exception, method: str, url: str, status_code: int, message: str):
        self.status_code = status_code
        self.error = error
        self.url = url
        self.request = type("Request", (), {"method": method})()
        self._text = message

    def json(self):
        return {"error": self._text}

    @property
    def text(self):
        return self._text


def _handle_exception(err, method, url):
    # Handle specific request exceptions and provide meaningful status codes/messages
    if isinstance(err, InvalidURL):
        return ErrorResponse(err, method, url, status_code=400, message="Invalid URL: malformed API URL.")
    if isinstance(err, ConnectionError):
        return ErrorResponse(err, method, url, status_code=503, message="Connection error: unable to reach the server.")
    elif isinstance(err, Timeout):
        return ErrorResponse(err, method, url, status_code=408, message="Request timed out: the server took too long to respond.")
    elif isinstance(err, HTTPError):
        return ErrorResponse(err, method, url, status_code=500, message="HTTP error: invalid response from the server.")
    elif isinstance(err, RequestException):
        return ErrorResponse(err, method, url, status_code=503, message="Request error: an error occurred while making the request.")
    return ErrorResponse(err, method, url, status_code=500, message=f"Unexpected error: {str(err)}")


def _request(method, route, data=None, params=None):
    url = f"{BASE_URL}{route}"
    if params:
        query = urlencode({key: value for key, value in params.items() if value is not None})
        if query:
            separator = "&" if "?" in url else "?"
            url = f"{url}{separator}{query}"
    try:
        return requests.request(method, url, json=data, timeout=TIMEOUT)
    except Exception as err:
        return _handle_exception(err, method, url)


def post(route, data):
    return _request("POST", route, data)


def delete(route):
    return _request("DELETE", route)


def patch(route, data):
    return _request("PATCH", route, data)


def put(route, data=None):
    return _request("PUT", route, data)


def get(route, params=None):
    return _request("GET", route, params=params)
