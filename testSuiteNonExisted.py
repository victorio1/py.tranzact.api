import requests
import json

ENDPOINT = "http://api.countrylayer.com/v2"
API_KEY = "8b01b8f5121bf963476455fc22a4b79f"
COUNTRY = "/UU"

def test_can_call_endpoint():
    url = ENDPOINT + COUNTRY
    params = {
        'access_key': API_KEY
    }
    response = requests.get(url, params=params)    
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
    
    try:
        error_response = response.json()
        print("Error Response:", json.dumps(error_response, indent=4))
        if "status" in error_response:
            assert error_response["status"] == 404, f"Expected status 404, but got {error_response['status']}"
        else:
            print("La clave 'status' no se encontró en la respuesta.")        
        if "message" in error_response:
            assert error_response["message"] == "Not Found", f"Expected message 'Not Found', but got {error_response['message']}"
        else:
            print("La clave 'message' no se encontró en la respuesta.")        
    except json.JSONDecodeError:
        print("La respuesta no es un JSON válido.")

    print("Error handling assertions completed.")

test_can_call_endpoint()
