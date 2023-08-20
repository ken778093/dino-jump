import pygame
from random import randint

win = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

# font = pygame.font.Font(None, 36)
# win_hi = font.render('you escape,for now...', False, (0, 225, 0))
# lose = font.render('does im need to say more???', False, (225, 0, 0))
# mes = win_hi


background = pygame.image.load("boom.jpg")
background = pygame.transform.scale(background, (700, 500))
dinosaur=pygame.transform.scale(pygame.image.load("turtle.png"), (75, 75))
dinosaur_rect = dinosaur.get_rect()
dinosaur_rect.x =10
dinosaur_rect.y = 400

class bomb(pygame.sprite.Sprite):
    def __init__(self, x, y,):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("jump!.jpg"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
    def draw(self, surface):
        surface.blit(self.image,self.rect)

boom1 = bomb(75, 450)
boom2 = bomb(175, 450)
boom3 = bomb(275, 450)
boom4 = bomb(375, 450)
boom5 = bomb(475, 450)
boom6 = bomb(575, 450)

boom_list =[boom1, boom2,boom3, boom4,boom5, boom6]

run = True
vy = 0
dinosaur_rect.y -= vy
while run:
    keys = pygame.key.get_pressed()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if keys[pygame.K_SPACE]:
                    vy=5

        
    if dinosaur_rect.y < 190:
            vy -= 10
        





        
    win.blit(background, (0, 0))
    win.blit(dinosaur, dinosaur_rect)
    for b in boom_list:
        b.draw(win)
        if dinosaur_rect.colliderect(b.rect):
            game_over = True
            # mes = lose

    pygame.display.update()
    clock.tick(60)