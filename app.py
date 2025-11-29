import streamlit as st
import googlemaps
from googlemaps.convert import decode_polyline
import folium
from streamlit_folium import st_folium
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Configuration
st.set_page_config(page_title="Trajectoire Kinshasa", layout="wide", initial_sidebar_state="expanded")

# Titre
st.title("🗺️ Trajet Optimal : Rond Point Victoire → Gare Centrale")
st.markdown("Projet L4 Data Science - Graphe d'optimisation d'itinéraire")

# ====== SIDEBAR ======
st.sidebar.header("📋 Informations du Projet")

st.sidebar.write("### 🎓 Université")
st.sidebar.write("Université Protestante au Congo (UPC)")
st.sidebar.write("Faculté des Sciences de l’Information")

st.sidebar.write("### 👥 Équipe du Projet (L4 Data Science)")
st.sidebar.write("- Nkura Kikakala Winner")
st.sidebar.write("- Mbala Lepu Djessy")
st.sidebar.write("- Wasso Kisembe Victorina")

st.sidebar.write("### 📘 Promotion")
st.sidebar.write("Licence 4 — Data Science")

# ====== RÉCUPÉRER CLÉ API ======
api_key = st.secrets["GOOGLE_MAPS_API_KEY"]

gmaps = googlemaps.Client(key=api_key)

# ====== COORDONNÉES DES ARRÊTS ======
points = {
    "Rond-Point Victoire": "-4.327760,15.313710",
    "Bongolo": "-4.322700,15.309500",
    "Hôpital Général": "-4.319190,15.306300",
    "Marché Central": "-4.316000,15.303000",
    "Boulevard 30 Juin": "-4.313200,15.298500",
    "Gare Centrale": "-4.312100,15.287900"
}

# ====== RÉCUPÉRER LE TRAJET ======
try:
    route = gmaps.directions(
        origin=points["Rond-Point Victoire"],
        destination=points["Gare Centrale"],
        waypoints=[
            points["Bongolo"],
            points["Hôpital Général"],
            points["Marché Central"],
            points["Boulevard 30 Juin"]
        ],
        mode="driving"
    )

    st.success("✔ Trajet récupéré avec succès !")

except Exception as e:
    st.error(f"❌ Erreur : {e}")
    st.stop()

# ====== AFFICHER LES INFORMATIONS DU TRAJET ======
col1, col2, col3 = st.columns(3)

with col1:
    leg = route[0]['legs'][0]
    st.metric("📏 Distance", leg['distance']['text'])

with col2:
    st.metric("⏱️ Durée", leg['duration']['text'])

with col3:
    st.metric("🛑 Arrêts", "5")

# ====== SECTION 1 : CARTE INTERACTIVE ======
st.subheader("1️⃣ Carte du Trajet")

# Décoder le polyline
polyline = route[0]['overview_polyline']['points']
coords = decode_polyline(polyline)

# Créer la carte
m = folium.Map(location=[-4.32, 15.30], zoom_start=14)

# Tracer le trajet
points_list = [(c['lat'], c['lng']) for c in coords]
folium.PolyLine(points_list, weight=5, opacity=0.8, color='blue').add_to(m)

# Ajouter les marqueurs
colors = ['green', 'blue', 'blue', 'blue', 'blue', 'red']
for i, (name, coord) in enumerate(points.items()):
    lat, lng = map(float, coord.split(','))
    icon = "play" if i == 0 else ("stop" if i == len(points)-1 else "info")
    folium.Marker(
        [lat, lng],
        popup=name,
        tooltip=name,
        icon=folium.Icon(color=colors[i], icon=icon)
    ).add_to(m)

st_folium(m, width=700, height=500)

# ====== SECTION 2 : GRAPHE ORIENTÉ ======
st.subheader("2️⃣ Graphe Orienté des Arrêts")

# Créer le graphe
G = nx.DiGraph()
arrets = list(points.keys())
G.add_nodes_from(arrets)

edges = [
    (arrets[0], arrets[1]),
    (arrets[1], arrets[2]),
    (arrets[2], arrets[3]),
    (arrets[3], arrets[4]),
    (arrets[4], arrets[5])
]
G.add_edges_from(edges)

# Afficher le graphe
fig, ax = plt.subplots(figsize=(12, 6))
pos = nx.spring_layout(G, seed=42, k=2)
nx.draw(G, pos, with_labels=True, node_size=2000, font_size=9,
        arrows=True, arrowsize=20, node_color='lightblue',
        edge_color='gray', width=2, ax=ax)
st.pyplot(fig)

# ====== SECTION 3 : DÉTAILS DU TRAJET ======
st.subheader("3️⃣ Détails des Étapes")

steps = route[0]['legs'][0]['steps']
for i, step in enumerate(steps, 1):
    with st.expander(f"Étape {i}: {step['html_instructions']}", expanded=False):
        st.write(f"📏 Distance : {step['distance']['text']}")
        st.write(f"⏱️ Durée : {step['duration']['text']}")

# ====== SECTION 4 : TABLEAU DES ARRÊTS ======
st.subheader("4️⃣ Liste des Arrêts")

arrets_df = pd.DataFrame({
    "Arrêt": list(points.keys()),
    "Latitude": [float(coord.split(',')[0]) for coord in points.values()],
    "Longitude": [float(coord.split(',')[1]) for coord in points.values()]
})

st.dataframe(arrets_df, use_container_width=True)

# ====== FOOTER ======
st.divider()
st.markdown("🚀 *Projet d'optimisation d'itinéraire avec Google Maps API*")
st.markdown("*Déployé sur Streamlit Cloud*")
