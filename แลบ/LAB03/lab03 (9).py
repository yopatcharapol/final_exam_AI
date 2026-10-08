import heapq

# # Define the cities and distances between them
cities = ["กรุงเทพฯ", "นครสวรรค์", "แพร่", "เชียงใหม่", "พะเยา"]

# # fronzenset is similar to set but fronzenset is immutable and hashable
distances = {
    frozenset(["กรุงเทพฯ", "นครสวรรค์"]): 240,
    frozenset(["กรุงเทพฯ", "แพร่"]): 520,
    frozenset(["กรุงเทพฯ", "เชียงใหม่"]): 700,
    frozenset(["กรุงเทพฯ", "พะเยา"]): 780,
    frozenset(["นครสวรรค์", "แพร่"]): 320,
    frozenset(["นครสวรรค์", "เชียงใหม่"]): 460,
    frozenset(["นครสวรรค์", "พะเยา"]): 480,
    frozenset(["แพร่", "เชียงใหม่"]): 200,
    frozenset(["แพร่", "พะเยา"]): 140,
    frozenset(["เชียงใหม่", "พะเยา"]): 150
}
# cities = ["กรุงเทพฯ", "นครสวรรค์", "แพร่", "เชียงใหม่", "พะเยา", "Lampang", "Lamphun", "Uttaradit", "Sukhothai", "Tak"]
# distances = {
#      frozenset(["กรุงเทพฯ", "นครสวรรค์"]): 240,
#      frozenset(["กรุงเทพฯ", "แพร่"]): 520,
#      frozenset(["กรุงเทพฯ", "เชียงใหม่"]): 700,
#      frozenset(["กรุงเทพฯ", "พะเยา"]): 780,
#      frozenset(["กรุงเทพฯ", "Lampang"]): 600,
#      frozenset(["กรุงเทพฯ", "Lamphun"]): 670,
#      frozenset(["กรุงเทพฯ", "Uttaradit"]): 490,
#      frozenset(["กรุงเทพฯ", "Sukhothai"]): 410,
#      frozenset(["กรุงเทพฯ", "Tak"]): 430,
#      frozenset(["นครสวรรค์", "แพร่"]): 320,
#      frozenset(["นครสวรรค์", "เชียงใหม่"]): 460,
#      frozenset(["นครสวรรค์", "พะเยา"]): 480,
#      frozenset(["นครสวรรค์", "Lampang"]): 360,
#      frozenset(["นครสวรรค์", "Lamphun"]): 430,
#      frozenset(["นครสวรรค์", "Uttaradit"]): 250,
#      frozenset(["นครสวรรค์", "Sukhothai"]): 170,
#      frozenset(["นครสวรรค์", "Tak"]): 190,
#      frozenset(["แพร่", "เชียงใหม่"]): 200,
#      frozenset(["แพร่", "พะเยา"]): 140,
#      frozenset(["แพร่", "Lampang"]): 220,
#      frozenset(["แพร่", "Lamphun"]): 250,
#      frozenset(["แพร่", "Uttaradit"]): 110,
#      frozenset(["แพร่", "Sukhothai"]): 150,
#      frozenset(["แพร่", "Tak"]): 180,
#      frozenset(["เชียงใหม่", "พะเยา"]): 150,
#      frozenset(["เชียงใหม่", "Lampang"]): 100,
#      frozenset(["เชียงใหม่", "Lamphun"]): 30,
#      frozenset(["เชียงใหม่", "Uttaradit"]): 250,
#      frozenset(["เชียงใหม่", "Sukhothai"]): 270,
#      frozenset(["เชียงใหม่", "Tak"]): 280,
#      frozenset(["พะเยา", "Lampang"]): 170,
#      frozenset(["พะเยา", "Lamphun"]): 180,
#      frozenset(["พะเยา", "Uttaradit"]): 210,
#      frozenset(["พะเยา", "Sukhothai"]): 240,
#      frozenset(["พะเยา", "Tak"]): 250,
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

# Start at กรุงเทพฯ
start_city = "กรุงเทพฯ"
route, total_distance = greedy_best_first_search(start_city, cities, distances)

print(route)
print(total_distance)
