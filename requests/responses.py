from config import base_url, post_pet_body
import requests
import os
import json


def post_pet():
    url = base_url + '/pet/'
    payload = post_pet_body
    response = requests.post(url, json=payload)
    return response


def open_json(path):
    cur_dir = os.path.dirname(__file__)
    path_to_json = os.path.join(cur_dir, path)
    schema = json.loads(open(path_to_json).read())
    return schema


def put_pet():
    url = base_url + '/pet'
    payload = post_pet_body
    response = requests.put(url, json=payload)
    return response


def delete_pet():
    post_resp = post_pet()
    pet_id = post_resp.json()
    url = base_url +'/pet/'+ str(pet_id['id'])
    response = requests.delete(url)
    return response
  
  