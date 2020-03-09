import folium
import pandas as pd
from folium import plugins
import numpy as np
from folium.plugins import HeatMap
heatmap = folium.Map(location=[17.5427787, 78.5719924],control_scale=True, zoom_start=5)


dataset = pd.read_csv('dataset.csv')
dataset.head()
print(dataset.columns)




for index, row in dataset.iterrows():
    folium.CircleMarker([row['Latitude'], row['Longitude']],
                        radius=10,
                        popup=row['Restaurant Name'],
                        fill_color="#3db7e4", # divvy color
                       ).add_to(heatmap)

stationArr = dataset[['Latitude', 'Longitude']].values
heatmap.add_child(plugins.HeatMap(stationArr, radius=30))
heatmap.save('heatmap.html')
