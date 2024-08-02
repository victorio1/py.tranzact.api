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

def call_uk():
    countries = load_countries_from_file('allcountries.json')
    country_name = "United Kingdom of Great Britain and Northern Ireland"
    country_data = find_country_by_name(countries, country_name)

    if country_data:
        print(json.dumps(country_data, indent=4))
        
        # Realiza las aserciones para verificar cada campo del objeto del Reino Unido
        assert country_data["name"] == "United Kingdom of Great Britain and Northern Ireland"
        assert country_data["topLevelDomain"] == [".uk"]
        assert country_data["alpha2Code"] == "GB"
        assert country_data["alpha3Code"] == "GBR"
        assert country_data["callingCodes"] == ["44"]
        assert country_data["capital"] == "London"
        assert country_data["altSpellings"] == ["GB", "UK", "Great Britain"]
        assert country_data["region"] == "Europe"
        
        print("All assertions for the United Kingdom passed successfully.")
    else:
        print(f"Country '{country_name}' is not in the file.")

if __name__ == "__main__":
    call_uk()
