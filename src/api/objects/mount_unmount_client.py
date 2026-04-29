import requests
from src.config import BASE_URL

def post(route, data):

    url = f"{BASE_URL}{route}"

    response = requests.post(url,data)

    return response

def delete(route):

    url = f"{BASE_URL}{route}"

    response = requests.delete(url)

    return response
