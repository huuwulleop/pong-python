import pygame, sys

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <= 0 or ball.bottom >= screen_heigth:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
    

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

ball_speed_x = 7
ball_speed_y = 7

# Main game loop
while True:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    ball_animation()
    
    # Draw rectangles
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_heigth))
    
    # Update the window
    pygame.display.flip()
    clock.tick(60) # Limit the game to 60FPS
