import sender_stand_request
from data import KitBody


def assert_request(kit_body):
    response = sender_stand_request.send_post_request(kit_body)

    assert response.status_code == 201
    assert response.json().get("name") == kit_body["name"]
    assert response.json().get("authToken") != ""

def assert_negative_request(kit_body):
    response = sender_stand_request.send_post_request(kit_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos" \
                                         "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres" \


def test_kit_name_1_letters_success_response():
    # Positive Test Case 1: The allowed number of characters (1)
    kit_body = KitBody.kit_body_1
    assert_request(kit_body)

def test_kit_name_511_letters_success_response():
    # Positive Test Case 2: The allowed number of characters (511)
    kit_body = KitBody.kit_body_2
    assert_request(kit_body)

def test_kit_name_0_letters_error_response():
    # Negative Test Case 3: The number of characters is less than the allowed amount (0)
    kit_body = KitBody.kit_body_3
    assert_negative_request(kit_body)

def test_kit_name_512_letters_error_response():
    # Negative Test Case 4: The number of characters is greater than the allowed amount (512)
    kit_body = KitBody.kit_body_4
    assert_negative_request(kit_body)

def test_kit_name_special_symbols_error_response():
    # Negative Test Case 5: Special characters are allowed
    kit_body = KitBody.kit_body_5
    assert_request(kit_body)

def test_kit_name_has_spaces_error_response():
    # Negative Test Case 6: Spaces are allowed
    kit_body = KitBody.kit_body_6
    assert_request(kit_body)

def test_kit_name_has_numbers_success_response():
    # Negative Test Case 7: Numbers are allowed
    kit_body = KitBody.kit_body_7
    assert_request(kit_body)

def test_param_is_not_passed_error_response():
    # Negative Test Case 8: The parameter is not passed in the request
    kit_body = KitBody.kit_body_8.copy()
    kit_body.pop("name")
    assert_negative_request(kit_body)

def test_different_param_is_passed_error_response():
    # Negative Test Case 9: A different parameter type is passed (number)
    kit_body = KitBody.kit_body_9
    assert_negative_request(kit_body)
