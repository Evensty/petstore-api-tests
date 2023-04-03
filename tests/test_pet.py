import requests

from config import base_url
from jsonschema import validate
from requests.responses import post_pet, put_pet, delete_pet, open_json


class TestPet:

    def test_post_pet_check_status(self):
        response = post_pet()
        assert response.status_code == 200

    def test_post_pet_check_name(self):
        response = post_pet()
        response_body = response.json()
        assert response_body['name'] == 'sharky'

    # def test_post_pet_invalid_value():
    #   url = base_url + '/pet'
    #   payload = invalid_value
    #   response = requests.post(url, json=payload)
    #   assert response.status_code == 405, response.json()

    def test_post_pet_validate_schema(self):
        response = post_pet()
        schema = open_json('../schemas/post_pet.json')
        response_body = response.json()
        validate(response_body, schema)

    def test_get_pet_check_status(self):
        post_resp = post_pet()
        pet_id = post_resp.json()
        url = base_url + "/pet/" + str(pet_id['id'])
        print(url)
        response = requests.get(url)
        assert response.status_code == 200, response.text

    def test_get_pet_check_name(self):
        post_resp = post_pet()
        pet_id = post_resp.json()
        url = base_url +'/pet/'+ str(pet_id['id'])
        response = requests.get(url)
        pet_name = response.json()
        assert pet_name['name'] == 'sharky'

    def test_get_pet_check_category(self):
        post_resp = post_pet()
        pet_id = post_resp.json()
        url = base_url +'/pet/'+ str(pet_id['id'])
        response = requests.get(url)
        pet_category = response.json()
        assert pet_category['category']['name'] == 'longdog'

    def test_put_pet_check_status(self):
        response = put_pet()
        assert response.status_code == 200

    def test_put_pet_check_tag_name(self):
        response = put_pet()
        tag_name = response.json()
        assert tag_name['tags'][0]['name'] == 'some_tag'

    def test_pet_should_be_deleted(self):
        response = delete_pet()
        assert response.status_code == 200

    def test_pet_delete_check_status(self):
        delete_resp = delete_pet()
        deleted_pet = delete_resp.json()
        url = base_url +'/pet/'+ str(deleted_pet['message'])
        response = requests.get(url)
        assert response.status_code == 404

    

  
  
  
  
  