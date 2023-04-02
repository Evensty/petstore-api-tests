from config import base_url, post_pet_body
import requests
import pytest


@pytest.fixture(scope='session')
def post_pet():
    url = base_url + '/pet'
    payload = post_pet_body
    response = requests.post(url, json=payload)
    return response