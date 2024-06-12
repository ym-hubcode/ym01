
import pygame

def draw_network(screen, topology):
    for router_id, router_info in topology.items():
        position = router_info["position"]
        pygame.draw.circle(screen, (0, 0, 255), position, 10)
        for neighbor_id in router_info["links"]:
            neighbor_position = topology[neighbor_id]["position"]
            pygame.draw.line(screen, (0, 0, 0), position, neighbor_position)
