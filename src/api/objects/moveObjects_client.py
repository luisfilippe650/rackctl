from src.config import BASE_URL
import requests

def post(route, data):

    url = f"{BASE_URL}{route}"

    response = requests.post(url,data)

    return response
