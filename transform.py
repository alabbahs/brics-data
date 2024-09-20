import json
import pandas as pd
from rich import print


def clean_data(data):
    rows = []

    for country_data in data:
        country = country_data['country']
        indicators = country_data['indicators']

        rows.extend(
            {
                "country": country,
                "indicator_id": indicator['indicator']['id'],
                "indicator_value": indicator['indicator'].get('value', None),
                "year": indicator['date'],
                "value": indicator['value']
            }
            for i in range(10)
            for indicator in indicators[i][1]
        )

    return rows


def to_csv(df):
    df.to_csv('data/countries_indicators.csv', index=False)


if __name__ == "__main__":

    with open("data/countries_indicators.json", "r") as file:
        data = json.load(file)

    df = pd.DataFrame(clean_data(data))
    to_csv(df)

    print("cleaned data saved to data/countries_indicators.csv")
