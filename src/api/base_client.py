from requests.exceptions import ConnectionError, Timeout, HTTPError
from src.utils.configuration import BASE_URL, TIMEOUT
import requests


def post(route, data):
    try:
        url = f"{BASE_URL}{route}"
        response = requests.post(url, json=data, timeout=TIMEOUT)
        return response

    except (ConnectionError, Timeout, HTTPError) as err:
        return err


def delete(route):
    try:
        url = f"{BASE_URL}{route}"
        response = requests.delete(url, timeout=TIMEOUT)
        return response

    except (ConnectionError, Timeout, HTTPError) as err:
        return err


def patch(route, data):
    try:
        url = f"{BASE_URL}{route}"
        response = requests.patch(url, json=data, timeout=TIMEOUT)
        return response

    except (ConnectionError, Timeout, HTTPError) as err:
        return err


def put(route):
    try:
        url = f"{BASE_URL}{route}"
        response = requests.put(url, timeout=TIMEOUT)
        return response

    except (ConnectionError, Timeout, HTTPError) as err:
        return err


def get(route):
    try:
        url = f"{BASE_URL}{route}"
        response = requests.get(url, timeout=TIMEOUT)
        return response

    except (ConnectionError, Timeout, HTTPError) as err:
        return err