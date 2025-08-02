import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

            # Lista de comprobación del Proyecto Sprint 7
#prueba1 positiva usando el positive assert
def test_1_crear_un_kit_con_1_letra():
    new_kit_body = get_kit_body("A")
    positive_assert(new_kit_body)

#prueba2 usando el numero maximo permitido de caracteres
def test_2_crear_un_kit_con_511_caracteres():
    new_kit_body = get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(new_kit_body)

#prueba 3 negativa usando el negative assert
def test_3_creación_de_un_kit_con_0_caracteres():
    new_kit_body = get_kit_body("")
    negative_assert(new_kit_body)

#prueba 4 se excede el numero de caracteres permitidos
def test_4_creación_de_un_kit_usando_512_caracteres():
    new_kit_body = get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcd"
                                "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(new_kit_body)

#prueba5 positiva usando caracteres especiales
def test_5_crear_un_kit_con_caracteres_especiales():
    new_kit_body = get_kit_body("№%@")
    positive_assert(new_kit_body)

#prueba6 positiva usando espacios
def test_6_crear_un_kit_usando_caracteres_y_espacios():
    new_kit_body = get_kit_body(" A Aaa ")
    positive_assert(new_kit_body)

#prueba7 positiva permitiendo usar numeros en una string
def test_7_crear_un_kit_usando_numeros():
    new_kit_body = get_kit_body("456")
    positive_assert(new_kit_body)

#prueba 8 negativa usando el negative assert
def test8_creación_un_kit_sin_parametros():
    new_kit_body = {}
    negative_assert(new_kit_body)

#prueba 9 negativa usando numeros en el parametro
def test9_crear_un_kit_con_numeros_enteros_en_el_nombre():
    new_kit_body = get_kit_body(123)
    negative_assert(new_kit_body)
