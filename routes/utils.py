from django.conf import settings
import json
import heapq

def get_data():
		with open(settings.CONF_PATH, 'r') as config_file:
			config_data = json.load(config_file)
		departure = config_data["departure"]
		autonomy = config_data["autonomy"]
		return departure, autonomy

def find_fastes_algo(routes, autonomy, departure, arrival):
	graph ={}
	for route in routes:
		graph.setdefault(route.origin, []).append((route.destination, route.travel_time))
		graph.setdefault(route.destination, []).append((route.origin, route.travel_time))
	
	pq = [(0, departure, [departure], autonomy)]
	visited = set()

	while pq:
		current_time, current_planet, path, fuel_left = heapq.heappop(pq)

		if current_planet == arrival:
			return current_time, path
		if (current_planet, fuel_left) in visited:
			continue
		visited.add((current_planet, fuel_left))

		for neighbor, travel_time in graph.get(current_planet, []):
			if fuel_left >= travel_time:
				heapq.heappush(pq, (current_time + travel_time, neighbor, path + [neighbor], fuel_left - travel_time))
			else:
				heapq.heappush(pq, (current_time + travel_time + 1, neighbor, path + [neighbor], autonomy - travel_time))
	return float('inf')
				 
				  
		 
			  
		
	

	  