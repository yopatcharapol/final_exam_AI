
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

# cities = ["กรุงเทพฯ", "นครสวรรค์", "แพร่", "เชียงใหม่", "พะเยา", "Lampang", "Lamphun", "Uttaradit", "Sukhothai", "Tak"]
# distances = {
#     ("กรุงเทพฯ", "นครสวรรค์"): 240,
#     ("กรุงเทพฯ", "แพร่"): 520,
#     ("กรุงเทพฯ", "เชียงใหม่"): 700,
#     ("กรุงเทพฯ", "พะเยา"): 780,
#     ("กรุงเทพฯ", "Lampang"): 600,
#     ("กรุงเทพฯ", "Lamphun"): 670,
#     ("กรุงเทพฯ", "Uttaradit"): 490,
#     ("กรุงเทพฯ", "Sukhothai"): 410,
#     ("กรุงเทพฯ", "Tak"): 430,
#     ("นครสวรรค์", "แพร่"): 320,
#     ("นครสวรรค์", "เชียงใหม่"): 460,
#     ("นครสวรรค์", "พะเยา"): 480,
#     ("นครสวรรค์", "Lampang"): 360,
#     ("นครสวรรค์", "Lamphun"): 430,
#     ("นครสวรรค์", "Uttaradit"): 250,
#     ("นครสวรรค์", "Sukhothai"): 170,
#     ("นครสวรรค์", "Tak"): 190,
#     ("แพร่", "เชียงใหม่"): 200,
#     ("แพร่", "พะเยา"): 140,
#     ("แพร่", "Lampang"): 220,
#     ("แพร่", "Lamphun"): 250,
#     ("แพร่", "Uttaradit"): 110,
#     ("แพร่", "Sukhothai"): 150,
#     ("แพร่", "Tak"): 180,
#     ("เชียงใหม่", "พะเยา"): 150,
#     ("เชียงใหม่", "Lampang"): 100,
#     ("เชียงใหม่", "Lamphun"): 30,
#     ("เชียงใหม่", "Uttaradit"): 250,
#     ("เชียงใหม่", "Sukhothai"): 270,
#     ("เชียงใหม่", "Tak"): 280,
#     ("พะเยา", "Lampang"): 170,
#     ("พะเยา", "Lamphun"): 180,
#     ("พะเยา", "Uttaradit"): 210,
#     ("พะเยา", "Sukhothai"): 240,
#     ("พะเยา", "Tak"): 250,
#     ("Lampang", "Lamphun"): 40,
#     ("Lampang", "Uttaradit"): 140,
#     ("Lampang", "Sukhothai"): 170,
#     ("Lampang", "Tak"): 200,
#     ("Lamphun", "Uttaradit"): 170,
#     ("Lamphun", "Sukhothai"): 200,
#     ("Lamphun", "Tak"): 230,
#     ("Uttaradit", "Sukhothai"): 70,
#     ("Uttaradit", "Tak"): 100,
#     ("Sukhothai", "Tak"): 90
# }

# Create a function to find the nearest neighbor
def find_nearest_neighbor(current_city, unvisited_cities, distances):
    nearest_city = None
    min_distance = float('inf')
    for city in unvisited_cities:
        distance = distances.get((current_city, city)) \
            or distances.get((city, current_city))
        if distance < min_distance:
            min_distance = distance
            nearest_city = city
    return nearest_city, min_distance

# Greedy algorithm to solve TSP using the Nearest Neighbor approach
def greedy_tsp(start_city, cities, distances):
    unvisited_cities = set(cities)
    unvisited_cities.remove(start_city)
    current_city = start_city
    route = [start_city]
    total_distance = 0
    
    while unvisited_cities:
        next_city, distance = \
            find_nearest_neighbor(current_city, unvisited_cities, distances)
        route.append(next_city)
        total_distance += distance
        current_city = next_city
        unvisited_cities.remove(next_city)
    
    # Return to the starting city
    return_distance = distances.get((current_city, start_city)) \
        or distances.get((start_city, current_city))
    route.append(start_city)
    total_distance += return_distance
    
    return route, total_distance

# Start at กรุงเทพฯ
start_city = "กรุงเทพฯ"
route, total_distance = greedy_tsp(start_city, cities, distances)

print(route)
print(total_distance)

