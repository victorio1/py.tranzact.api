import requests
import json

ENDPOINT = "http://api.countrylayer.com/v2/all"
API_KEY = "8b01b8f5121bf963476455fc22a4b79f"

def find_country_by_name(countries, country_name):
    for country in countries:
        if country.get("name") == country_name:
            return country
    return None

def test_can_call_endpoint():
    params = {
        'access_key': API_KEY
    }
    response = requests.get(ENDPOINT, params=params)    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    countries = response.json()
    albania = find_country_by_name(countries, "Ukraine")
    
    if albania:
        print("Datos de Albania:", json.dumps(albania, indent=4))
    else:
        print("El país no se encontró.")

test_can_call_endpoint()
