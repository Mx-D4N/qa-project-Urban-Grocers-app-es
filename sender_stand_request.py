import configuration
import data
import requests

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body, headers=data.headers)

def post_new_client_kit(kit_body, auth_token):
    new_headers = data.headers.copy()
    new_headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body, headers=new_headers)
