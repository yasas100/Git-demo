import pygame
import ast
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
done = False
screen.fill((255, 255, 255))

lines = [line.rstrip('\n') for line in open('Names.txt')]
font = pygame.font.SysFont("comicsansms", 25)

for i in range(1,len(lines),2):
    text = font.render(lines[i-1], True, eval(lines[i]))
    screen.blit(text,(10,i*20))
  

pygame.display.flip()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    
   
    clock.tick(60)
pygame.quit()  