import folium
from folium import plugins
import random
import time

# Create a map centered around the world
world_map = folium.Map(location=[0, 0], zoom_start=2)

# Create a marker cluster to hold dynamic markers
marker_cluster = plugins.MarkerCluster().add_to(world_map)

# Function to generate random data points
def generate_random_data():
    return [random.uniform(-180, 180), random.uniform(-90, 90)]

# Update the map with new data points and save it after each update
while True :  # Update forever
    location = generate_random_data()
    #location= [36.8065, 10.1815]
    # Create a CircleMarker with a red dot and a tooltip showing the latitude and longitude
    marker = folium.CircleMarker(
        location=location,
        radius=5,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=1,
        tooltip=f"Lng: {location[0]}, Lat: {location[1]}"
    )
    marker.add_to(marker_cluster)
    
    # Save the map with a unique name for each update
    world_map.save("dynamic_world_map.html")
    
    time.sleep(0.5)  # Sleep for 0.5 seconds before the next update
