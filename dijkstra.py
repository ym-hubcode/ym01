
import heapq

def dijkstra(network_topology, start_router):
    queue = []
    heapq.heappush(queue, (0, start_router))
    distances = {router: float('inf') for router in network_topology}
    distances[start_router] = 0
    visited = set()
    
    while queue:
        current_distance, current_router = heapq.heappop(queue)
        
        if current_router in visited:
            continue
        
        visited.add(current_router)
        
        for neighbor, weight in network_topology[current_router].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances
