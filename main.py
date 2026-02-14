import pygame



pygame.init()
screen  = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
running = True

dt  = 0

def mag(vecX, vecY):
    return (vecX**2 + vecY**2)**0.5



player_pos = [400, 400]
chaser_pos = [10, 10]

chaser_path = [chaser_pos]



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
    
    chaser_pos[0] += vector_to_player[0] * 40 * dt
    chaser_pos[1] += vector_to_player[1] * 40 * dt
    chaser_path.append([chaser_pos[0], chaser_pos[1]])
    
    if (keys[pygame.K_w] or keys[pygame.K_UP]) :
        player_pos[1] -= 50*dt
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) :
        player_pos[1] += 50*dt
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) :
        player_pos[0] -= 50*dt
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) :
        player_pos[0] += 50*dt
        
    if(player_pos[0] < 0) :
        player_pos[0] = 800
    elif(player_pos[0] > 800) :
        player_pos[0] = 0
        
    if(player_pos[1] < 0) :
        player_pos[1] = 800
    elif(player_pos[1] > 800) :
        player_pos[1] = 0
        
        
        
    
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000  # Convert milliseconds to seconds
    
pygame.quit()