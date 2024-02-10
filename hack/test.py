from urllib.request import urlopen
import json
with open('geojson.json') as response:
    counties = json.load(response)
    print(counties)
# with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
#     counties = json.load(response)

# import pandas as pd
# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
#                    dtype={"fips": str})

import plotly.express as px

fig = px.choropleth(
    geojson=counties,color_continuous_scale="Viridis",
                    )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
