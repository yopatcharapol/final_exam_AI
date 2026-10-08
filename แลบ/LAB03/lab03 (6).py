import networkx as nx
from matplotlib import pyplot as plt

import matplotlib.font_manager as fm

# require setting fonts
font_path = "Fonts/THSarabunNew.ttf"
# thai_font = fm.FontProperties(fname=font_path)
thai_font = fm.FontProperties(fname=font_path)

# searching font if it exists
for f in fm.findSystemFonts(fontpaths=None, fontext='ttf'):
    if 'thai' in f.lower() or 'sarabun' in f.lower():
        print(f)

# Define the cities and distances between them
cities = ["กรุงเทพฯ", "นครสวรรค์", "แพร่", "เชียงใหม่", "พะเยา"]
distances = {
    ("กรุงเทพฯ", "นครสวรรค์"): 240,
    ("กรุงเทพฯ", "แพร่"): 520,
    ("กรุงเทพฯ", "เชียงใหม่"): 700,
    ("กรุงเทพฯ", "พะเยา"): 780,
    ("นครสวรรค์", "แพร่"): 320,
    ("นครสวรรค์", "เชียงใหม่"): 460,
    ("นครสวรรค์", "พะเยา"): 480,
    ("แพร่", "เชียงใหม่"): 200,
    ("แพร่", "พะเยา"): 140,
    ("เชียงใหม่", "พะเยา"): 150
}

coordinates = {
    "กรุงเทพฯ": (0, 0),
    "นครสวรรค์": (0, 240),
    "แพร่": (100, 520),
    "เชียงใหม่": (-50, 680),
    "พะเยา": (100, 650)
}

# cities = [
#     "กรุงเทพฯ",
#     "นครสวรรค์",
#     "แพร่",
#     "เชียงใหม่",
#     "พะเยา",
#     "Lampang",
#     "Lamphun",
#     "Uttaradit",
#     "Sukhothai",
#     "Tak",
# ]
# # distances = {
# #     ("กรุงเทพฯ", "นครสวรรค์"): 240,
# #     ("กรุงเทพฯ", "แพร่"): 520,
# #     ("กรุงเทพฯ", "เชียงใหม่"): 700,
# #     ("กรุงเทพฯ", "พะเยา"): 780,
# #     ("กรุงเทพฯ", "Lampang"): 600,
# #     ("กรุงเทพฯ", "Lamphun"): 670,
# #     ("กรุงเทพฯ", "Uttaradit"): 490,
# #     ("กรุงเทพฯ", "Sukhothai"): 410,
# #     ("กรุงเทพฯ", "Tak"): 430,
# #     ("นครสวรรค์", "แพร่"): 320,
# #     ("นครสวรรค์", "เชียงใหม่"): 460,
# #     ("นครสวรรค์", "พะเยา"): 480,
# #     ("นครสวรรค์", "Lampang"): 360,
# #     ("นครสวรรค์", "Lamphun"): 430,
# #     ("นครสวรรค์", "Uttaradit"): 250,
# #     ("นครสวรรค์", "Sukhothai"): 170,
# #     ("นครสวรรค์", "Tak"): 190,
# #     ("แพร่", "เชียงใหม่"): 200,
# #     ("แพร่", "พะเยา"): 140,
# #     ("แพร่", "Lampang"): 220,
# #     ("แพร่", "Lamphun"): 250,
# #     ("แพร่", "Uttaradit"): 110,
# #     ("แพร่", "Sukhothai"): 150,
# #     ("แพร่", "Tak"): 180,
# #     ("เชียงใหม่", "พะเยา"): 150,
# #     ("เชียงใหม่", "Lampang"): 100,
# #     ("เชียงใหม่", "Lamphun"): 30,
# #     ("เชียงใหม่", "Uttaradit"): 250,
# #     ("เชียงใหม่", "Sukhothai"): 270,
# #     ("เชียงใหม่", "Tak"): 280,
# #     ("พะเยา", "Lampang"): 170,
# #     ("พะเยา", "Lamphun"): 180,
# #     ("พะเยา", "Uttaradit"): 210,
# #     ("พะเยา", "Sukhothai"): 240,
# #     ("พะเยา", "Tak"): 250,
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
# #      "กรุงเทพฯ": (13.7563, 100.5018),
# #     "นครสวรรค์": (15.7040, 100.1370),
# #     "แพร่": (18.1446, 100.1407),
# #     "เชียงใหม่": (18.7883, 98.9853),
# #     "พะเยา": (19.1922, 99.8788),
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

# plt.rcParams['font.family'] = 'TH Sarabun New'
# plt.rcParams['font.family'] = prop.get_name()
# plt.rc('font', family='TH Sarabun New')
plt.figure(figsize=(12, 8))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    node_color="lightblue",
    font_size=20,
    font_weight="bold",
    edge_color="gray",
    font_family=thai_font.get_name()
)

print(thai_font.get_name())
# # Draw edge labels
edge_labels = {
    (city1, city2): f"{distance} กม." for (city1, city2), distance in distances.items()
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_family=thai_font.get_name(), font_size=18)

# Display the graph
plt.title('กราฟแสดงผลลัพธ์', fontproperties ='TH Sarabun New' )
# plt.text(0.5, 0.5, "เชียงใหม่", fontproperties='TH Sarabun New', fontsize=20)
# plt.title("Distances Between Cities for Traveling Salesman Problem")
plt.show()
