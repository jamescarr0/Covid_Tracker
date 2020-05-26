import requests
from operator import attrgetter

from covid_data import CovidData


class CovidApi:
    """ A general class to manage the Covid-19 API request. """

    def __init__(self):
        """ Initialise class attributes. """

        self.url = "https://corona-api.com/countries"
        self.headers = {"content-type": "application/json"}
        self.countries = []
        self.missing_coordinates = []

    def call_api(self):
        """ request data from API and print the status code. """

        request = (requests.get(self.url, headers=self.headers))
        print(f"\nStatus code: {request.status_code}")

        # Process the request
        self._process_data(request)

    def _process_data(self, request):
        """ Process the data and convert to json format. """

        request_data = request.json()

        # Construct country objects.
        self._construct_country_objects(request_data['data'])

    def _construct_country_objects(self, data_dict):
        """ Build a list of country objects with country specific covid-19 data. """

        for country in data_dict:
            # Do not add countries with missing coordinates to the list.
            # Coordinate data is used to plot information on a world map.
            if country['coordinates']['longitude'] == 0 and country['coordinates']['latitude'] == 0:
                # Add the country with missing coordinates to a list.
                self.missing_coordinates.append(country['name'])
                continue

            covid = CovidData(country['name'], country['population'], country['latest_data']['confirmed'],
                              country['latest_data']['deaths'], country['coordinates']['longitude'],
                              country['coordinates']['latitude'])

            self.countries.append(covid)

        # Sort countries alphabetically.
        self._sort_alphabetically()

    def _sort_alphabetically(self):
        """ Sort objects alphabetically by country. """
        self.countries = sorted(self.countries, key=attrgetter('country'))

    def print_summary(self):
        """ Print a summary of the API data. """
        for country in self.countries:
            # Format rate to a percentage to 1dp.
            mortality_rate = "{:.1f}%".format(country.mortality_rate)

            print(f"\n{country.country}")
            print(f"\tPopulation: {country.population}")
            print(f"\tConfirmed: {country.confirmed}")
            print(f"\tDeaths: {country.deaths}")
            print(f"\tMortality rate: {mortality_rate}")
