import configuration
import requests
import data


def post_new_user(body):  # crear nuevo usuario
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)

def get_token():  # obtener authtoken
    response_data = response.json()
    return response_data['authToken']

auth_token = get_token()

# Imprimir el token
print("authToken:", auth_token)

def send_post_request(kit_body):
    auth_token = get_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, headers=headers,
                             json=kit_body)

    return response

print(response.status_code)