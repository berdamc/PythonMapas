import folium
import pandas as pd
from folium import plugins

mapa = folium.Map(
    location=[-26.9918,-52.5133],
    tiles='Stamen Terrain',
    zoom_start=10
)


#Coordenadas GPS no click
mapa.add_child(folium.LatLngPopup())

#lendo CSV
df = pd.read_csv("olist_geolocation_dataset.csv")

df2 = df.sample(frac = 0.001)

coordenadas=[]
for lat,lng in zip(df2.geolocation_lat.values[:10000],df2.geolocation_lng.values[:10000]):
  coordenadas.append([lat,lng])

mapa = folium.Map(location=[-15.788497, -47.879873], zoom_start=5, tiles='Stamen Toner')
mapa.add_child(plugins.HeatMap(coordenadas))

#salvando o resultado em arquivo HTML
mapa.save('teste.html')
