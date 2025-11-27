import googlemaps
from datetime import datetime

# --- INSERER VOTRE CLE API ---
gmaps = googlemaps.Client(key="AIzaSyDFNjE5G_S4i0XHlh3fLUIarAv7LToyXOk")

# Coordonnées GPS (approximatives) des arrêts
points = {
    "victoire": "-4.327760,15.313710",
    "bongolo": "-4.322700,15.309500",
    "mama_yemo": "-4.319190,15.306300",
    "marche_central": "-4.316000,15.303000",
    "bd_30_juin": "-4.313200,15.298500",
    "gare_centrale": "-4.312100,15.287900"
}

# Appel à l’API Directions
route = gmaps.directions(
    origin=points["victoire"],
    destination=points["gare_centrale"],
    waypoints=[
        points["bongolo"],
        points["mama_yemo"],
        points["marche_central"],
        points["bd_30_juin"]
    ],
    mode="driving"
)

print("Trajet récupéré avec succès !")
print(route[0]['legs'])
