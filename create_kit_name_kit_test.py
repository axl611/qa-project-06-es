import sender_stand_request
from data import KitBody

def assert_kit_request(kit_body, expected_status, error_message=None):
    response = sender_stand_request.send_kit_creation_request(kit_body)
    assert response.status_code == expected_status

    if expected_status == 201:
        assert response.json().get("name") == kit_body["name"]
        assert response.json().get("authToken") != ""
    else:
        assert response.json()["code"] == 400
        assert response.json()["message"] == error_message

def test_create_kit_1_letter_in_name_success_response():
    # Positive Test Case 1: The allowed number of characters (1)
    kit_body = KitBody.kit_body_1
    assert_kit_request(kit_body, 201)

def test_create_kit_511_letter_in_name_success_response():
    # Positive Test Case 2: The allowed number of characters (511)
    kit_body = KitBody.kit_body_2
    assert_kit_request(kit_body, 201)

def test_create_kit_0_letter_in_name_success_response():
    # Negative Test Case 3: The number of characters is less than the allowed amount (0)
    kit_body = KitBody.kit_body_3
    assert_kit_request(kit_body, 400, "No se han aprobado todos los parámetros requeridos El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres")

def test_create_kit_512_letter_in_name_success_response():
    # Negative Test Case 4: The number of characters is greater than the allowed amount (512)
    kit_body = KitBody.kit_body_4
    assert_kit_request(kit_body, 400, "No se han aprobado todos los parámetros requeridos El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres")

def test_create_kit_has_special_symbol_in_name_get_sucess_response():
    # Negative Test Case 5: Special characters are allowed
    kit_body = KitBody.kit_body_5
    assert_kit_request(kit_body, 201)

def test_create_kit_has_spaces_in_name_get_error_response():
    # Negative Test Case 6: Spaces are allowed
    kit_body = KitBody.kit_body_6
    assert_kit_request(kit_body, 201)

def test_create_kit_has_numbers_in_name_get_sucess_response():
    # Negative Test Case 7: Numbers are allowed
    kit_body = KitBody.kit_body_7
    assert_kit_request(kit_body, 201)

def test_create_kit_parameter_not_passed_in_request_error_response():
    # Negative Test Case 8: The parameter is not passed in the request
    kit_body = KitBody.kit_body_8.copy()
    kit_body.pop("name")
    assert_kit_request(kit_body, 400, "No se han aprobado todos los parámetros requeridos El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres")

def test_create_kit_different_param_type_passed_error_response():
    # Negative Test Case 9: A different parameter type is passed (number)
    kit_body = KitBody.kit_body_9
    assert_kit_request(kit_body, 400, "No se han aprobado todos los parámetros requeridos El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres")