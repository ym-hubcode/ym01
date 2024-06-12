
from router import Router
from network import Network
from utils.visualization import draw_network
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    network = Network()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        draw_network(screen, network.topology)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
