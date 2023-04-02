base_url = 'https://petstore.swagger.io/v2'
post_pet_body = {
  "id": 334,
  "category": {
    "id": 556,
    "name": 'longdog'
  },
  "name": "sharky",
  "photoUrls": [
    "some_photo"
  ],
  "tags": [
    {
      "id": 71,
      "name": "some_tag"
    }
  ],
  "status": "available"
}

invalid_value = {
  "id": 334,
  "category": {
    "id": 556,
    "name": 1
  },
  "name": "sharky",
  "photoUrls": [
    "some_photo"
  ],
  "tags": [
    {
      "id": 71,
      "name": "some_tag"
    }
  ],
  "status": "available"
}