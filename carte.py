import googlemaps
import folium
from googlemaps.convert import decode_polyline
import os
from dotenv import load_dotenv

load_dotenv()

# --- Récupérer la clé depuis .env ---
api_key = os.getenv("GOOGLE_MAPS_API_KEY")
if not api_key:
    print("❌ Clé API non trouvée dans .env")
    exit()

gmaps = googlemaps.Client(key=api_key)

# Coordonnées GPS des lieux
points = {
    "victoire": "-4.327760,15.313710",
    "bongolo": "-4.322700,15.309500",
    "mama_yemo": "-4.319190,15.306300",
    "marche_central": "-4.316000,15.303000",
    "bd_30_juin": "-4.313200,15.298500",
    "gare_centrale": "-4.312100,15.287900"
}

# --- Récupérer le trajet via Google Maps Directions API ---
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

# Vérification rapide
if not route:
    print("❌ Le trajet n'a pas été récupéré. Vérifie ta clé API et l'activation de l'API Directions.")
    exit()

print("✔ Trajet récupéré avec succès !")

# --- Extraire le polyline et décoder les coordonnées ---
polyline = route[0]['overview_polyline']['points']
coords = decode_polyline(polyline)

# --- Création de la carte centrée sur Kinshasa ---
m = folium.Map(location=[-4.32, 15.30], zoom_start=14)

# --- Tracer le trajet ---
points_list = [(c['lat'], c['lng']) for c in coords]
folium.PolyLine(points_list, weight=5, opacity=0.8, color='blue').add_to(m)

# --- Ajouter les marqueurs pour chaque arrêt ---
for name, coord in points.items():
    lat, lng = map(float, coord.split(","))
    folium.Marker([lat, lng], popup=name).add_to(m)

# --- Sauvegarder la carte dans un fichier HTML ---
m.save("trajet_victoire_gare.html")
print("✔ Carte générée : trajet_victoire_gare.html")