from covid_api import CovidApi
from covid_visual import CovidVisual

# Create instance.
cva = CovidApi()

# Make an api request and process data.
cva.call_api()

# Print summary of the data processed.
cva.print_summary()

# Create a world map visual.
cv_vis = CovidVisual(cva)
