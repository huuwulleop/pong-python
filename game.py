import pygame, sys

# Setup
pygame.init()
clock = pygame.time.Clock()

# Setup window
screen_width = 1280
screen_heigth = 960
screen = pygame.display.set_mode((screen_width, screen_heigth))
pygame.display.set_caption("Pong")




# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Update the window
    pygame.display.flip()
    clock.tick(60) # Limit the game to 60FPS
