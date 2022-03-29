import pygame, sys

# Setup
pygame.init()
clock = pygame.time.Clock()

# Setup window
screen_width = 1280
screen_heigth = 960
screen = pygame.display.set_mode((screen_width, screen_heigth))
pygame.display.set_caption("Pong")

ball_w = 30
ball_h = 30

ball = pygame.Rect(screen_width/2 - ball_w/2, screen_heigth/2 - ball_h/2, ball_w, ball_h)
player = pygame.Rect(screen_width - 20, screen_heigth/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_heigth/2 - 70, 10, 140)

bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

# Main game loop
while True:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Draw rectangles
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_heigth))
    
    
    # Update the window
    pygame.display.flip()
    clock.tick(60) # Limit the game to 60FPS
