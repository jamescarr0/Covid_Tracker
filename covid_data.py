class CovidData:
    """ A class to store a country's covid-19 data. """

    def __init__(self, country, population, confirmed, deaths, lon, lat):
        self.country = country
        self.population = population
        self.confirmed = confirmed
        self.deaths = deaths
        self.longitude = lon
        self.latitude = lat

        self.mortality_rate = self._calc_mortality()

    def _calc_mortality(self):
        """
            Calculate mortality rate.
            Catch the zero division error when data is missing.
            returns int: mortality rate
        """
        try:
            mr = self.deaths / self.confirmed * 100.0
        except ZeroDivisionError:
            mr = 0
        return mr
