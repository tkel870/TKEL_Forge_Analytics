import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
from db_connect import get_connection

conn = get_connection()

# Load edges
edges = pd.read_sql_query("""
SELECT match_id_a, match_id_b, shared_strength
FROM shared_matches
""", conn)

# Load clusters
clusters = pd.read_sql_query("""
SELECT match_id, cluster_id
FROM match_clusters
""", conn)

# Load match strength (cM)
matches = pd.read_sql_query("""
SELECT match_id, cm_total
FROM matches
""", conn)

conn.close()

print("Building graph...")
G = nx.Graph()

# Filter weak edges to reduce visual chaos
EDGE_MIN = 0.50   # increase to 0.60 if still messy

for _, row in edges.iterrows():
    weight = float(row["shared_strength"])
    if weight >= EDGE_MIN:
        G.add_edge(row["match_id_a"], row["match_id_b"], weight=weight)

print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

# Maps
cluster_map = dict(zip(clusters.match_id, clusters.cluster_id))
cm_map = dict(zip(matches.match_id, matches.cm_total))

# Node colors by cluster
node_colors = [cluster_map.get(node, -1) for node in G.nodes()]

# Node sizes by DNA strength
node_sizes = []
for node in G.nodes():
    cm = cm_map.get(node, 10)
    node_sizes.append(max(30, min(300, cm * 2.2)))

print("Drawing network...")
plt.figure(figsize=(18, 12))

# Layout (increase k for more spacing)
pos = nx.spring_layout(G, k=0.38, seed=870)

nx.draw_networkx_nodes(
    G,
    pos,
    node_size=node_sizes,
    node_color=node_colors,
    cmap=plt.cm.tab10,
    alpha=0.90
)

nx.draw_networkx_edges(G, pos, alpha=0.10)

plt.title("Forensic Genetic Genealogy Network Clusters (Synthetic Case)", fontsize=18)
plt.axis("off")

# Save high-res image
out_dir = os.path.join(os.path.dirname(__file__), "..", "visuals")
os.makedirs(out_dir, exist_ok=True)

png_path = os.path.join(out_dir, "fgg_network_clusters.png")
plt.savefig(png_path, dpi=300, bbox_inches="tight")

print("\nSaved network image to:")
print(png_path)

plt.show()
