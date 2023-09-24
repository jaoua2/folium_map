# folium_map
visualise a map with markers based on folium, code created with the help of chatgpt.

dynamic_map_cursor generates random red dots on the map, you can change the generation algorithm and make it like a trajectory, it also gives the position of marked dots when you hover the mouse's cursor on them.
map_csv visualises red dots on the map based on coordinates from a CSV file.
they both generate .html file as output.

the sample.json is taken from https://samples.adsbexchange.com/traces/2023/08/01/00/trace_full_009400.json
you can use json_to_csv.py to extract longitude,latitude and altitude from the json file and exploit them
the output is flight_data.csv
