import os
import requests
import json
from rich import print

# Define country codes for BRICS and Western competitors TEST
countries = ["BR", "RU", "IN", "CN", "ZA", "US", "GB", "FR", "DE"]

# Define the 10 important economic metrics (indicator codes)
indicators = [
    "NY.GDP.MKTP.CD",     # GDP (current USD)
    "NY.GDP.PCAP.CD",     # GDP per capita
    "SL.UEM.TOTL.ZS",     # Unemployment rate
    "FP.CPI.TOTL.ZG",     # Inflation (consumer prices)
    "NY.GNP.PCAP.CD",     # GNI per capita (Atlas method)
    "DT.DOD.DECT.CD",     # External debt
    "GC.DOD.TOTL.GD.ZS",  # Government debt to GDP
    "NE.RSB.GNFS.CD",     # Trade balance
    "SP.DYN.LE00.IN",     # Life expectancy (proxy for HDI)
    "BX.KLT.DINV.CD.WD"   # Foreign direct investment (net inflows)
]

base_url = "https://api.worldbank.org/v2/country/{}/indicator/{}?format=json"


def get_indicators(indicators, countries) -> list:
    all_data = []
    for country in countries:
        country_data = {}
        country_data['country'] = country
        country_data['indicators'] = []

        for indicator in indicators:
            url = base_url.format(country, indicator)
            response = requests.get(url)
            country_data["indicators"].append(response.json())

        all_data.append(country_data)

    return all_data


def create_json(data):
    if not os.path.exists("data"):
        os.makedirs("data")

    with open("data/countries_indicators.json", "w") as file:
        file.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    data = get_indicators(indicators, countries)
    create_json(data)
    print(f"Data saved successfully to 'data/countries_indicators.json'")