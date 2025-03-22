import pygame
from constants import *
from player import Player



def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print ("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    from player import Player
    player_obj = Player(x, y)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill the screen with black
        screen.fill((0, 0, 0))
        
        # Draw the player
        player_obj.draw(screen)

        # Refresh the screen
        pygame.display.flip()

        # Limit the frame rate to 60 FPS and get the delta time
        dt = clock.tick(60) / 1000  # Convert from milliseconds to seconds

        
        
    pygame.quit()


if __name__ == "__main__":
    main()