from src.config import BASE_URL
import requests

def post(route, data):
    url = f"{BASE_URL}{route}"

    response = requests.post(url, json=data)

    return response

def delete(route):
    url = f"{BASE_URL}{route}{data}"

    response = requests.delete(url)

    return response

def get(route):
    url = f"{BASE_URL}{route}"

    response = requests.get(url)

    return response

def get_rows(route):

    url = f"{BASE_URL}{route}"

    response = requests.get(url)

    return response
