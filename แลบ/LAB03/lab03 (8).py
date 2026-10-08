import heapq

# # Define the cities and distances between them
# cities = ["Bangkok", "Nakhon Sawan", "Phrae", "Chiang Mai", "Phayao"]

# # fronzenset is similar to set but fronzenset is immutable and hashable
# distances = {
#     frozenset(["Bangkok", "Nakhon Sawan"]): 240,
#     frozenset(["Bangkok", "Phrae"]): 520,
#     frozenset(["Bangkok", "Chiang Mai"]): 700,
#     frozenset(["Bangkok", "Phayao"]): 780,
#     frozenset(["Nakhon Sawan", "Phrae"]): 320,
#     frozenset(["Nakhon Sawan", "Chiang Mai"]): 460,
#     frozenset(["Nakhon Sawan", "Phayao"]): 480,
#     frozenset(["Phrae", "Chiang Mai"]): 200,
#     frozenset(["Phrae", "Phayao"]): 140,
#     frozenset(["Chiang Mai", "Phayao"]): 150
# }
# cities = ["Bangkok", "Nakhon Sawan", "Phrae", "Chiang Mai", "Phayao", "Lampang", "Lamphun", "Uttaradit", "Sukhothai", "Tak"]
# distances = {
#      frozenset(["Bangkok", "Nakhon Sawan"]): 240,
#      frozenset(["Bangkok", "Phrae"]): 520,
#      frozenset(["Bangkok", "Chiang Mai"]): 700,
#      frozenset(["Bangkok", "Phayao"]): 780,
#      frozenset(["Bangkok", "Lampang"]): 600,
#      frozenset(["Bangkok", "Lamphun"]): 670,
#      frozenset(["Bangkok", "Uttaradit"]): 490,
#      frozenset(["Bangkok", "Sukhothai"]): 410,
#      frozenset(["Bangkok", "Tak"]): 430,
#      frozenset(["Nakhon Sawan", "Phrae"]): 320,
#      frozenset(["Nakhon Sawan", "Chiang Mai"]): 460,
#      frozenset(["Nakhon Sawan", "Phayao"]): 480,
#      frozenset(["Nakhon Sawan", "Lampang"]): 360,
#      frozenset(["Nakhon Sawan", "Lamphun"]): 430,
#      frozenset(["Nakhon Sawan", "Uttaradit"]): 250,
#      frozenset(["Nakhon Sawan", "Sukhothai"]): 170,
#      frozenset(["Nakhon Sawan", "Tak"]): 190,
#      frozenset(["Phrae", "Chiang Mai"]): 200,
#      frozenset(["Phrae", "Phayao"]): 140,
#      frozenset(["Phrae", "Lampang"]): 220,
#      frozenset(["Phrae", "Lamphun"]): 250,
#      frozenset(["Phrae", "Uttaradit"]): 110,
#      frozenset(["Phrae", "Sukhothai"]): 150,
#      frozenset(["Phrae", "Tak"]): 180,
#      frozenset(["Chiang Mai", "Phayao"]): 150,
#      frozenset(["Chiang Mai", "Lampang"]): 100,
#      frozenset(["Chiang Mai", "Lamphun"]): 30,
#      frozenset(["Chiang Mai", "Uttaradit"]): 250,
#      frozenset(["Chiang Mai", "Sukhothai"]): 270,
#      frozenset(["Chiang Mai", "Tak"]): 280,
#      frozenset(["Phayao", "Lampang"]): 170,
#      frozenset(["Phayao", "Lamphun"]): 180,
#      frozenset(["Phayao", "Uttaradit"]): 210,
#      frozenset(["Phayao", "Sukhothai"]): 240,
#      frozenset(["Phayao", "Tak"]): 250,
#      frozenset(["Lampang", "Lamphun"]): 40,
#      frozenset(["Lampang", "Uttaradit"]): 140,
#      frozenset(["Lampang", "Sukhothai"]): 170,
#      frozenset(["Lampang", "Tak"]): 200,
#      frozenset(["Lamphun", "Uttaradit"]): 170,
#      frozenset(["Lamphun", "Sukhothai"]): 200,
#      frozenset(["Lamphun", "Tak"]): 230,
#      frozenset(["Uttaradit", "Sukhothai"]): 70,
#      frozenset(["Uttaradit", "Tak"]): 100,
#      frozenset(["Sukhothai", "Tak"]): 90
# }

def heuristic(current_city, unvisited_cities, distances):
    if not unvisited_cities:
        return 0
    nearest_distance = float('inf')
    for city in unvisited_cities:
        distance = distances[frozenset([current_city, city])]
        if distance < nearest_distance:
            nearest_distance = distance
    return nearest_distance


def greedy_best_first_search(start_city, cities, distances):
    unvisited_cities = set(cities)
    unvisited_cities.remove(start_city)
    current_city = start_city
    route = [start_city]
    total_distance = 0
    
    while unvisited_cities:
        # Find the nearest neighbor using the heuristic
        next_city = None
        min_heuristic = float('inf')
        for city in unvisited_cities:
            distance = distances[frozenset([current_city, city])]
            h = heuristic(city, unvisited_cities - {city}, distances) + distance
            if h < min_heuristic:
                min_heuristic = h
                next_city = city
        
        # Move to the next city
        route.append(next_city)
        total_distance += distances[frozenset([current_city, next_city])]
        current_city = next_city
        unvisited_cities.remove(next_city)
    
    # Return to the starting city
    return_distance = distances[frozenset([current_city, start_city])]
    route.append(start_city)
    total_distance += return_distance
    
    return route, total_distance

# Start at Bangkok
start_city = "Bangkok"
route, total_distance = greedy_best_first_search(start_city, cities, distances)

print(route)
print(total_distance)
