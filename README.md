# README - Projet Trajectoire : Graphe d'Optimisation d'Itinéraire

## Objectif

Trouver le chemin optimal pour un véhicule qui part du Rond Point Victoire et arrive à la Gare Centrale en passant par tous les arrêts intermédiaires. Le projet utilise Google Maps API pour calculer les trajets et Folium pour les visualiser sur une carte.

---

## Equipe

- Nkura Kikakala Winner
- Mbala Lepu Djessy
- Wasso Kisembe Victorina

Promo : L4 Data Science

---

## Structure du Projet

```
trajectoire/
├── victoire.py                 # Script principal - Appel à Google Maps API
├── graphe.py                   # Visualisation du graphe orienté
├── carte.py                    # Génération de la carte HTML
├── trajet_victoire_gare.html  # Carte interactive (généré)
├── requirements.txt            # Dépendances
└── README.md                   # Documentation
```

---

## Installation

### 1. Installer les dépendances

```powershell
pip install -r requirements.txt
```

### 2. Configurer Google Maps API

Créez un fichier `.env` :

```
GOOGLE_MAPS_API_KEY=YOUR_API_KEY_HERE
```

Obtenez votre clé sur [Google Cloud Console](https://console.cloud.google.com/) en activant Directions API et Maps JavaScript API.

---

## Utilisation

### Exécuter le script principal

```powershell
python victoire.py
```

Affiche les détails du trajet en console.

### Visualiser le graphe

```powershell
python graphe.py
```

Affiche le graphe orienté des arrêts.

### Générer la carte

```powershell
python carte.py
```

Crée `trajet_victoire_gare.html` - ouvrez dans un navigateur.

---

## Algorithme Utilisé

Google Maps Directions API (utilise Dijkstra/A* en interne) pour calculer le chemin optimal entre les arrêts.

---

## Arrêts du Trajet

1. Rond Point Victoire (départ)
2. Bongolo
3. Hôpital Général
4. Marché Central
5. Boulevard 30 Juin
6. Gare Centrale (arrivée)

