import random

import pygame

class Baobao(pygame.sprite.Sprite):
    def __init__(self):
        super(Baobao,self).__init__()
        self.image = pygame.image.load('material/images/baobao0.png').convert_alpha()
        self.images = [pygame.image.load('material/images/baobao{}.png'.format(i)).convert_alpha() for i in range(0,2)]
        self.dieimages = [pygame.image.load('material/images/diebaobao{}.png'.format(i)).convert_alpha() for i in range(0, 2)]
        self.attack_images = [pygame.image.load('material/images/attackbaobao{}.png'.format(i)).convert_alpha() for i in
                          range(0, 2)]
        self.rect = self.images[0].get_rect()
        self.rect.top = 25 + random.randrange(0,4)*125
        self.energy = 6
        self.rect.left = 1000
        self.speed = 5
        self.dietimes = 0
        self.isMeetWallNut = False
        self.isAlive = True

    def update(self, *args):
        if self.energy > 0:
            if self.isMeetWallNut:
                self.image = self.attack_images[args[0] % len(self.attack_images)]
            else:
                self.image = self.images[args[0] % len(self.images)]
            if self.rect.left > 250 and not self.isMeetWallNut:
                self.rect.left -= self.speed
        else:
            if self.dietimes < 2:
                print(self.dietimes, "没死")
                # self.image = self.dieimages[self.dietimes//2]
                self.image = self.dieimages[self.dietimes]
                self.dietimes += 1
            else:
                if self.dietimes > 30:
                    self.isAlive = False
                    self.kill()
                else:
                    self.dietimes += 1
