import pygame
import math
import random

pygame.init()
screen  = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
running = True

dt  = 0

def mag(vecX, vecY):
    return (vecX**2 + vecY**2)**0.5

dx = 0

def playerPath(time):
    return [350 + 100 * math.sin(time) + random.randint(0, dx),
            350 + 100 * math.cos(time) + random.randint(0, dx)]

player_pos = playerPath(0)
chaser_pos = [10, 10]


chaser_path = [chaser_pos]

speedChaser = 100


while running :
    
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
    screen.fill("black")
    
    keys = pygame.key.get_pressed()
    
    pygame.draw.circle(screen, "red", player_pos, 10)
    for path in chaser_path:
        pygame.draw.circle(screen, "yellow", path, 1)
        
    pygame.draw.circle(screen, "white", chaser_pos, 5)
    mag_to_player = mag(player_pos[0] - chaser_pos[0], player_pos[1] - chaser_pos[1])
    vector_to_player = [(player_pos[0] - chaser_pos[0])/mag_to_player,
                        (player_pos[1] - chaser_pos[1])/mag_to_player]
    
    
    
    
    chaser_pos[0] += vector_to_player[0] * speedChaser * dt
    chaser_pos[1] += vector_to_player[1] * speedChaser * dt
    chaser_path.append([chaser_pos[0], chaser_pos[1]])
    
    
    player_pos = playerPath(pygame.time.get_ticks() / 1000)
    
    
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000  # Convert milliseconds to seconds
    
pygame.quit()