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

with open("index.html", "w", encoding="utf-8") as f:
    f.write("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Projet NSI</title>
    <link rel="stylesheet" href="style.css"/>
    <link rel="script" href="script.js"/>
</head>
<body>
    <h1 class="title">Rechargez votre véhicule électrique à Angers <img src="assets/bolt.png" class="bolt" alt="Icone d'éclair"/></h1>
    <h3 class="description">Trouvez à Angers différentes bornes de recharge pour véhicules électriques, gratuites ou payantes.</h3>
    <main>
        <iframe class="map" id="map" width="1000" height="500" src="carte.html"></iframe>
        <div class="bottom">
            <p class="text">Il y a <span id="amount"></span> bornes de recharge <span id="type"></span> dans la ville</p>
            <div class="filter">
                <p>Filtrer</p>
                <div class="buttons">
                    <button id="free">Gratuites</button>
                    <button id="charged">Payantes</button>
                </div>
            </div>

        </div>
    </main>
    <a class="logo" href="https://www.angers.fr/" target="_blank"><img class="logo" src="assets/angers.webp" alt="Logo de la ville d'Angers"/></a>

    <img alt="Fond coloré" class="background" src="assets/gradient-bg.webp"/>

    <script>
    const freeButton = document.getElementById("free")
const chargedButton = document.getElementById("charged")
const map = document.getElementById("map")
const amount = document.getElementById("amount")
const type = document.getElementById("type")

const totalStations = %s
const freeStations = %s
const chargedStations = %s

amount.textContent = totalStations.toString()

freeButton.addEventListener("click", () => {
    chargedButton.classList.remove("active")
    if(freeButton.classList.contains("active")){
        freeButton.classList.remove("active")
        map.src = "./carte.html"
        amount.textContent = totalStations.toString()
        type.textContent = ""
    }else{
        freeButton.classList.add("active")
        map.src = "./carte_free.html"
        amount.textContent = freeStations.toString()
        type.textContent = "gratuites"
    }
})
chargedButton.addEventListener("click", () => {
    freeButton.classList.remove("active")
    if(chargedButton.classList.contains("active")){
        chargedButton.classList.remove("active")
        map.src = "./carte.html"
        amount.textContent = totalStations.toString()
        type.textContent = ""
    }else{
        chargedButton.classList.add("active")
        map.src = "./carte_charged.html"
        amount.textContent = chargedStations.toString()
        type.textContent = "payantes"
    }
})
</script>
</body>

</html>
    """ % (str(len(stations_payantes) + len(stations_gratuites)),
           str(len(stations_gratuites)),
           str(len(stations_payantes)))
            )
