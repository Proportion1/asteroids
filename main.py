import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    #added player before so there is something to add to the updateables and drawables group
    #player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateables, drawables)
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = (updateables,)
    Shot.containers = (shots, updateables, drawables)
    #added after because the lesson says to create all player objects after the change
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    #asteroid = Aster
    asteroid_field =  AsteroidField()
    

    
    #for player in updateables:
    #    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    #for player in drawables:
    #    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000
        for updates in updateables:
            updates.update(dt)

        for asteroid in asteroids:
            if(asteroid.collision(player)):
                print("Game over!")
                return
        
        #for shot in shots:
        #    if(shot.collision(player)):
        
            

        for draws in drawables:
            draws.draw(screen)
        pygame.display.flip()

    


if __name__ == "__main__":
    main()

