from dotenv import dotenv_values
from psycopg2.extensions import connection, cursor
import psycopg2
import pandas as pd
from pandas import DataFrame
from datetime import datetime

config = dotenv_values()

COUNTRY_NAMES = {"BR": 0, "RU": 1, "IN": 2, "CN": 3, "ZA": 4,
                 "US": 5, "GB": 6, "FR": 7, "DE": 8}

METRIC_TITLES = {"NY.GDP.MKTP.CD": 0,
                 "NY.GDP.PCAP.CD": 1,
                 "FP.CPI.TOTL.ZG": 2,
                 "NY.GNP.PCAP.CD": 3,
                 "DT.DOD.DECT.CD": 4,
                 "GC.DOD.TOTL.GD.ZS": 5,
                 "NE.RSB.GNFS.CD": 6,
                 "SP.DYN.LE00.IN": 7,
                 "BX.KLT.DINV.CD.WD": 8}


def get_connection() -> connection:
    """Establishes and returns a connection to the database."""
    conn = psycopg2.connect(
        dbname=config["DB_NAME"],
        user=config["DB_USER"],
        password=config["DB_PASSWORD"],
        host=config["DB_HOST"],
        port=config["DB_PORT"])
    return conn

def get_cursor(connection: connection) -> cursor:
    """Retrieves cursor from database connection"""
    cur = connection.cursor()
    return cur

def load_csv(csv) -> DataFrame:
    """Converts the csv data into pandas DataFrame format"""
    return pd.read_csv(csv)

def format_data(cur: cursor, data: DataFrame) -> None:
    country_name = COUNTRY_NAMES[data["country"]]
    metric_title = METRIC_TITLES[data["indicator_value"]]
    metric_value = float(data["value"])
    year = datetime.year(data["year"])

    cur.execute("LOAD TABLE Indicators ()")
    cur.close()
    return None

if __name__ == "__main__":
    conn = get_connection()
    cur = get_cursor()
    