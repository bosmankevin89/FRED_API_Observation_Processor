
#Imports
import requests
import configparser

class FRED_API_Observations:

    address = "https://api.stlouisfed.org/fred/series/observations"

    def __init__(self):

        try:
            # Set up the parameters we want to pass to the API.
            config = configparser.ConfigParser()
            config.read('config/config.ini')
            self.api_key = config['DEFAULT']['API_KEY']

            # Raise error on missing values
            if not self.api_key:
                raise ValueError('Configuration value "API_KEY" not defined')

        except ValueError as err:
            raise ValueError('Error initializing FRED_API_Observations: ' + str(err))

   
    def query(self, series_id, offset):
        parameters = {
            "file_type" : "json",
            "order_by": "observation_date",
            "sort_order": "asc",
            "api_key": self.api_key,
            "series_id" : series_id,
            "offset": offset
        }

        response = requests.get(self.address, params=parameters)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

        