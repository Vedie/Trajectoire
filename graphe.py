import networkx as nx
import matplotlib.pyplot as plt

# Création du graphe orienté
G = nx.DiGraph()

arrets = [
    "Rond-Point Victoire",
    "Bongolo",
    "Hôpital Général",
    "Marché Central",
    "Boulevard du 30 Juin",
    "Gare Centrale"
]

# Ajouter les arcs (trajets possibles)
edges = [
    ("Rond-Point Victoire", "Bongolo"),
    ("Bongolo", "Hôpital Général"),
    ("Hôpital Général", "Marché Central"),
    ("Marché Central", "Boulevard du 30 Juin"),
    ("Boulevard du 30 Juin", "Gare Centrale")
]

G.add_edges_from(edges)

# Dessiner le graphe
plt.figure(figsize=(10,5))
nx.draw(G, with_labels=True, node_size=3000, font_size=10, arrows=True)
plt.title("Graphe orienté : Victoire → Gare Centrale")
plt.show()
