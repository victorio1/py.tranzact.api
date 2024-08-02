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

def call_usa():
    countries = load_countries_from_file('allcountries.json')
    country_name = "United States of America"
    country_data = find_country_by_name(countries, country_name)

    if country_data:
        print(json.dumps(country_data, indent=4))
        
        assert country_data["name"] == "United States of America"
        assert country_data["topLevelDomain"] == [".us"]
        assert country_data["alpha2Code"] == "US"
        assert country_data["alpha3Code"] == "USA"
        assert country_data["callingCodes"] == ["1"]
        assert country_data["capital"] == "Washington, D.C."
        assert country_data["altSpellings"] == ["US", "USA", "United States of America"]
        assert country_data["region"] == "Americas"
        
        print("All assertions passed successfully.")
    else:
        print(f"Country '{country_name}' is not in the file.")

if __name__ == "__main__":
    call_usa()
