import folium
from folium import plugins
import pandas as pd

# Create a map centered around the world
world_map = folium.Map(location=[0, 0], zoom_start=2)

# Create a marker cluster to hold dynamic markers
marker_cluster = plugins.MarkerCluster().add_to(world_map)

# Read coordinates from a CSV file
coordinates_df = pd.read_csv('coordinates.csv')

# Iterate through the CSV data and add markers to the map
for index, row in coordinates_df.iterrows():
    location = [row['longitude'], row['latitude']]
    
    # Create a CircleMarker with a red dot and a tooltip showing the latitude and longitude
    marker = folium.CircleMarker(
        location=location,
        radius=5,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=1,
        tooltip=f"Lat: {location[0]}, Lng: {location[1]}"
    )
    marker.add_to(marker_cluster)

# Save the map
world_map.save("csv_coordinates_map.html")
