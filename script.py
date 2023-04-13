import csv
import folium

file = open("data.csv", "r")
lines = file.readlines()[1:]
stations_gratuites = []
stations_payantes = []

for row in lines:
    row = row.strip()
    gratuit, nom, x, y = row.split(",")
    if gratuit == "true":
        stations_gratuites.append({
            "name": nom,
            "x": x,
            "y": y
        })
    else:
        stations_payantes.append({
            "name": nom,
            "x": x,
            "y": y
        })
map = folium.Map(location=[47.47111573852694, -0.551897474884361], zoom_start=13, min_zoom=12)
map_free = folium.Map(location=[47.47111573852694, -0.551897474884361], zoom_start=13, min_zoom=12)
map_charged = folium.Map(location=[47.47111573852694, -0.551897474884361], zoom_start=13, min_zoom=12)

for station in stations_gratuites:
    folium.Marker(
        location=[station["x"], station["y"]],
        popup=station["name"],
        icon=folium.Icon(color="green"),
    ).add_to(map)
    folium.Marker(
        location=[station["x"], station["y"]],
        popup=station["name"],
        icon=folium.Icon(color="green"),
    ).add_to(map_free)

for station in stations_payantes:
    folium.Marker(
        location=[station["x"], station["y"]],
        popup=station["name"],
        icon=folium.Icon(color="blue"),
    ).add_to(map)
    folium.Marker(
        location=[station["x"], station["y"]],
        popup=station["name"],
        icon=folium.Icon(color="blue"),
    ).add_to(map_charged)

map.save("carte.html")
map_free.save("carte_free.html")
map_charged.save("carte_charged.html")

with open('amounts.txt', 'w') as f:
    f.write(str(len(stations_gratuites) + len(stations_payantes)) + "," + str(len(stations_gratuites)) + "," + str(len(stations_payantes)))

