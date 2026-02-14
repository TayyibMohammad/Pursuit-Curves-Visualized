import pygame
import math

mass1 = 1000000
# int(input("Mass of first body: "))
mass2 = 1000000
# int(input("Mass of second body: "))

posX1 = 100
# int(input("initial pos x of first body: "))
posY1 = 300
# int(input("initial pos y of first body: "))

posX2 = 100
# int(input("initial pos x of second body: "))
posY2 = 350
# int(input("initial pos y of second body: "))

def dist(vecX, vecY):
    return (vecX**2 + vecY**2)**0.5

vx1 =  math.sqrt((0.01*mass2)/dist(posX1-posX2, posY1-posY2))/2
# int(input("initial velocity vector x of first body: "))
vy1 = -1
# int(input("initial velocity vector y of first body: "))

vx2 = 0
# int(input("initial velocity vector x of second body: "))
vy2 = 0
# int(input("initial velocity vector y of second body: "))

# acceleration, velocity and postition are in [x-comp, y-comp] format


def calcSize(mass):
    return math.log10(mass);

size1 = calcSize(mass1)
size2 = calcSize(mass2)


maxDist = -1
minDist = 10000


# object 2 applies on object 1.
def force(pos1, pos2, m1, m2, G=0.01):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    
    # Calculate squared distance first to save a square root step if needed
    dist_sq = dx**2 + dy**2
    
    # Softening factor to prevent infinite force when objects overlap
    softening = 0.5 
    distance = math.sqrt(dist_sq + size1+size2)
    
    
    # Newton's Law: F = G * (m1 * m2) / r^2
    # Vector form: F_vec = (F / r) * displacement_vec
    mag_force = (G * m1 * m2) / (distance**2)
    
    force_x = (mag_force / distance) * dx
    force_y = (mag_force / distance) * dy
    
    return [force_x, force_y]
    

def acc(force , mass):
    return [(force[0])/mass, (force[1])/mass]

def newVec(acc, vec):
    return [vec[0] + acc[0]*dt, vec[1] + acc[1]*dt]
    

def newPos(vec, pos):
    
    return ([pos[0]+vec[0]*dt, pos[1]+vec[1]*dt])

pygame.init()
height = 700
width  = 1000
screen  = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

dt  = 0



pos1 = [posX1, posY1]
pos2 = [posX2, posY2]

vec1 = [vx1, vy1]
vec2 = [vx2, vy2]

paths = [pos1]



while running :
    
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
    screen.fill("black")
    
    keys = pygame.key.get_pressed()
    
    pygame.draw.circle(screen , "blue", pos1, size1)
    pygame.draw.circle(screen , "red", pos2, size2)
    for path in paths :
        pygame.draw.circle(screen , "yellow", path, 1)
    
    distance = dist(pos1[0]-pos2[0], pos1[1]-pos2[1])   
    minDist = min(minDist, distance)
    maxDist = max(maxDist, distance)
    
    pos1 = newPos(vec1, pos1)
    pos2 = newPos(vec2, pos2)
    
    paths.append(pos1.copy())
    
    forceOn1 = force(pos1, pos2, mass1, mass2)
    forceOn2 = [-1*forceOn1[0], -1*forceOn1[1]] # forceOn1
    
    acc1 = acc(forceOn1, mass1)
    acc2 = acc(forceOn2, mass2)
    
    vec1 = newVec(acc1, vec1)
    vec2 = newVec(acc2, vec2)
    
    if(pos1[0] < 0 or pos1[0] > width):
        vec1[0] *= -1
    
    if(pos1[1] < 0 or pos1[1] > height):
        vec1[1] *= -1
        
    if(pos2[0] < 0 or pos2[0] > width):
        vec2[0] *= -1
    
    if(pos2[1] < 0 or pos2[1] > height):
        vec2[1] *= -1
        
    
        
        
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000  # Convert milliseconds to seconds
    
print("Max Distance: ", maxDist)
print("Min Distance: ", minDist)
    
pygame.quit()