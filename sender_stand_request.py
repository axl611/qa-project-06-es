import configuration
import requests
import data


def create_new_user_request(body):  # crear nuevo usuario
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

user_response = create_new_user_request(data.user_body)
print(user_response.status_code)

def obtain_auth_token_from_response():  # obtener authtoken
    response_data = user_response.json()
    return response_data['authToken']

auth_token = obtain_auth_token_from_response()

# Imprimir el token
print("authToken:", auth_token)

def send_kit_creation_request(kit_body):
    auth_token = obtain_auth_token_from_response()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    kit_response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, headers=headers,
                             json=kit_body)

    return kit_response

print(user_response.status_code)