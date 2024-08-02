import json

def load_countries_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        countries = json.load(file)
    return countries

def find_country_by_name(countries, country_name):
    for country in countries:
        if country.get("name") == country_name:
            return country
    return None

def call_germany():
    countries = load_countries_from_file('allcountries.json')
    country_name = "Germany"
    country_data = find_country_by_name(countries, country_name)

    if country_data:
        print(json.dumps(country_data, indent=4))
        
        # Realiza las aserciones para verificar cada campo del objeto de Alemania
        assert country_data["name"] == "Germany"
        assert country_data["topLevelDomain"] == [".de"]
        assert country_data["alpha2Code"] == "DE"
        assert country_data["alpha3Code"] == "DEU"
        assert country_data["callingCodes"] == ["49"]
        assert country_data["capital"] == "Berlin"
        assert country_data["altSpellings"] == ["DE", "Federal Republic of Germany", "Bundesrepublik Deutschland"]
        assert country_data["region"] == "Europe"
        
        print("All assertions for Germany passed successfully.")
    else:
        print(f"Country '{country_name}' is not in the file.")

if __name__ == "__main__":
    call_germany()
