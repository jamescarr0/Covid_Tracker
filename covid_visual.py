from plotly.graph_objs import Layout
from plotly import offline


class CovidVisual:
    """ A class to manage plotting and displaying data on a world map. """

    def __init__(self, data):
        self.MAP_TITLE = "Covid-19 Tracker"
        self.data = data
        self._plot_covid()

    def _plot_covid(self):
        """ Create a visual representation of covid cases on a world map,
            save file as a html file and display on screen.
        """
        # Graph setup.
        graph_data = [{
            'type': 'scattergeo',
            'lon': [lon.longitude for lon in self.data.countries],
            'lat': [lat.latitude for lat in self.data.countries],
            'text': [self._hover_text(data) for data in self.data.countries],
            'marker': {
                'size': [2.5 * size.mortality_rate for size in self.data.countries],
                'color': [col.mortality_rate for col in self.data.countries],
                'colorscale': 'Bluered',
                'reversescale': False,
                'colorbar': {'title': 'Mortality rate %'}
            },
            'opacity': 0.8
        }]
        layout = Layout(title=self.MAP_TITLE)
        fig = {'data': graph_data, 'layout': layout}

        # Save world map as a html file and display.
        offline.plot(fig, filename='data/covid_map.html')

        # Print summary
        self._plot_summary()

    def _hover_text(self, data):
        """ Create a hover text label for the world map chart and return the created label.  """

        mortality_rate = "{:.1f}%".format(data.mortality_rate)
        label = f"Country: {data.country}<br>" \
                f"Population: {data.population}<br>" \
                f"Deaths: {data.deaths}<br>" \
                f"Mortality rate: {mortality_rate}"
        return label

    def _plot_summary(self):
        """
            Print the number of countries plotted on the world map and the number
            of countries with missing coordinates.
        """
        # Print individual countries missing coordinate data.
        for country in self.data.missing_coordinates:
            print(f"Missing coordinates for: {country}")

        # Print summary.
        print(f"\nTotal count: {len(self.data.missing_coordinates + self.data.countries)}")
        print(f"\t- {len(self.data.missing_coordinates)} countries with missing coordinates.\n"
              f"\t- {len(self.data.countries)} countries plotted on the world map.")
