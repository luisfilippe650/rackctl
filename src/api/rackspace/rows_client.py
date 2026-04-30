from src.config import BASE_URL
import requests

def post(route, data):

    url = f"{BASE_URL}{route}"
    response = requests.post(url, json=data)

    return response

def delete(route):

    url = f"{BASE_URL}{route}"
    response = requests.delete(url)

    return response

def delete_row_location(route):

    url = f"{BASE_URL}{route}"
    response = requests.delete(url)

    return response

def patch(route, data):

    url = f"{BASE_URL}{route},"
    response = requests.patch(url,json=data)

    return response

def put(route):

    url = f"{BASE_URL}{route}"
    response = requests.put(url)

    return response

def get(route):

    url = f"{BASE_URL}{route}"
    response = requests.get(url)

    return response

def get_racks(route):

    url = f"{BASE_URL}{route}"
    response = requests.get(url)

    return response



