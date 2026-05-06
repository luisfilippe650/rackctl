from requests.exceptions import ConnectionError, Timeout, HTTPError
from src.utils.configuration import BASE_URL, TIMEOUT
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
    if isinstance(err, ConnectionError):
        return ErrorResponse(err, method, url, status_code=503, message="Connection error: unable to reach the server.")
    elif isinstance(err, Timeout):
        return ErrorResponse(err, method, url, status_code=408, message="Request timed out: the server took too long to respond.")
    elif isinstance(err, HTTPError):
        return ErrorResponse(err, method, url, status_code=500, message="HTTP error: invalid response from the server.")
    return None


def post(route, data):
    url = f"{BASE_URL}{route}"
    try:
        return requests.post(url, json=data, timeout=TIMEOUT)
    except (ConnectionError, Timeout, HTTPError) as err:
        return _handle_exception(err, "POST", url)


def delete(route):
    url = f"{BASE_URL}{route}"
    try:
        return requests.delete(url, timeout=TIMEOUT)
    except (ConnectionError, Timeout, HTTPError) as err:
        return _handle_exception(err, "DELETE", url)


def patch(route, data):
    url = f"{BASE_URL}{route}"
    try:
        return requests.patch(url, json=data, timeout=TIMEOUT)
    except (ConnectionError, Timeout, HTTPError) as err:
        return _handle_exception(err, "PATCH", url)


def put(route):
    url = f"{BASE_URL}{route}"
    try:
        return requests.put(url, timeout=TIMEOUT)
    except (ConnectionError, Timeout, HTTPError) as err:
        return _handle_exception(err, "PUT", url)


def get(route):
    url = f"{BASE_URL}{route}"
    try:
        return requests.get(url, timeout=TIMEOUT)
    except (ConnectionError, Timeout, HTTPError) as err:
        return _handle_exception(err, "GET", url)