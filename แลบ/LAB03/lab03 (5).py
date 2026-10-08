import networkx as nx
from matplotlib import pyplot as plt

# Define the cities and distances between them
cities = ["Bangkok", "Nakhon Sawan", "Phrae", "Chiang Mai", "Phayao"]
distances = {
    ("Bangkok", "Nakhon Sawan"): 240,
    ("Bangkok", "Phrae"): 520,
    ("Bangkok", "Chiang Mai"): 700,
    ("Bangkok", "Phayao"): 780,
    ("Nakhon Sawan", "Phrae"): 320,
    ("Nakhon Sawan", "Chiang Mai"): 460,
    ("Nakhon Sawan", "Phayao"): 480,
    ("Phrae", "Chiang Mai"): 200,
    ("Phrae", "Phayao"): 140,
    ("Chiang Mai", "Phayao"): 150
}

coordinates = {
    "Bangkok": (0, 0),
    "Nakhon Sawan": (0, 240),
    "Phrae": (100, 520),
    "Chiang Mai": (-50, 680),
    "Phayao": (100, 650)
}

# cities = [
#     "Bangkok",
#     "Nakhon Sawan",
#     "Phrae",
#     "Chiang Mai",
#     "Phayao",
#     "Lampang",
#     "Lamphun",
#     "Uttaradit",
#     "Sukhothai",
#     "Tak",
# ]
# # distances = {
# #     ("Bangkok", "Nakhon Sawan"): 240,
# #     ("Bangkok", "Phrae"): 520,
# #     ("Bangkok", "Chiang Mai"): 700,
# #     ("Bangkok", "Phayao"): 780,
# #     ("Bangkok", "Lampang"): 600,
# #     ("Bangkok", "Lamphun"): 670,
# #     ("Bangkok", "Uttaradit"): 490,
# #     ("Bangkok", "Sukhothai"): 410,
# #     ("Bangkok", "Tak"): 430,
# #     ("Nakhon Sawan", "Phrae"): 320,
# #     ("Nakhon Sawan", "Chiang Mai"): 460,
# #     ("Nakhon Sawan", "Phayao"): 480,
# #     ("Nakhon Sawan", "Lampang"): 360,
# #     ("Nakhon Sawan", "Lamphun"): 430,
# #     ("Nakhon Sawan", "Uttaradit"): 250,
# #     ("Nakhon Sawan", "Sukhothai"): 170,
# #     ("Nakhon Sawan", "Tak"): 190,
# #     ("Phrae", "Chiang Mai"): 200,
# #     ("Phrae", "Phayao"): 140,
# #     ("Phrae", "Lampang"): 220,
# #     ("Phrae", "Lamphun"): 250,
# #     ("Phrae", "Uttaradit"): 110,
# #     ("Phrae", "Sukhothai"): 150,
# #     ("Phrae", "Tak"): 180,
# #     ("Chiang Mai", "Phayao"): 150,
# #     ("Chiang Mai", "Lampang"): 100,
# #     ("Chiang Mai", "Lamphun"): 30,
# #     ("Chiang Mai", "Uttaradit"): 250,
# #     ("Chiang Mai", "Sukhothai"): 270,
# #     ("Chiang Mai", "Tak"): 280,
# #     ("Phayao", "Lampang"): 170,
# #     ("Phayao", "Lamphun"): 180,
# #     ("Phayao", "Uttaradit"): 210,
# #     ("Phayao", "Sukhothai"): 240,
# #     ("Phayao", "Tak"): 250,
# #     ("Lampang", "Lamphun"): 40,
# #     ("Lampang", "Uttaradit"): 140,
# #     ("Lampang", "Sukhothai"): 170,
# #     ("Lampang", "Tak"): 200,
# #     ("Lamphun", "Uttaradit"): 170,
# #     ("Lamphun", "Sukhothai"): 200,
# #     ("Lamphun", "Tak"): 230,
# #     ("Uttaradit", "Sukhothai"): 70,
# #     ("Uttaradit", "Tak"): 100,
# #     ("Sukhothai", "Tak"): 90,
# # }

# # # Define coordinates for each city to reflect approximate distances
# # coordinates = {
# #      "Bangkok": (13.7563, 100.5018),
# #     "Nakhon Sawan": (15.7040, 100.1370),
# #     "Phrae": (18.1446, 100.1407),
# #     "Chiang Mai": (18.7883, 98.9853),
# #     "Phayao": (19.1922, 99.8788),
# #     "Lampang": (18.2888, 99.4968),
# #     "Lamphun": (18.5748, 99.0087),
# #     "Uttaradit": (17.6200, 100.0993),
# #     "Sukhothai": (17.0060, 99.8265),
# #     "Tak": (16.8833, 99.1256),
# # }

# Create a graph
G = nx.Graph()

# Add edges with distances
for (city1, city2), distance in distances.items():
    G.add_edge(city1, city2, weight=distance)

# Get positions for nodes based on coordinates
pos = coordinates

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    node_color="lightblue",
    font_size=12,
    font_weight="bold",
    edge_color="gray",
)

# Draw edge labels
edge_labels = {
    (city1, city2): f"{distance} km" for (city1, city2), distance in distances.items()
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

# Display the graph
plt.title("Distances Between Cities for Traveling Salesman Problem")
plt.show()
