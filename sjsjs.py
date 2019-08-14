############################################################################

# File name : detectSpriteCollsion.py

# Purpose : Demostarting The Killing of Sprite On Collision

# Usages : Logic can be used in real time games

# Start date : 04/01/2012

# End date : 04/01/2012

# Author : Ankur Aggarwal

# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html

# How To Run: python detectSpriteCollision.py

############################################################################


import pygame

from pygame.locals import *

import random

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

pygame.display.set_caption("Collision Detection")

clock = pygame.time.Clock()


# creating the boxes

class Boxes(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50, 50))

        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        self.rect = self.image.get_rect()

        self.rect.center = (random.randint(0, 640), random.randint(0, 480))
        self.x = self.rect.center[0]
        self.y = self.rect.center[1]
        self.speedx = random.randint(-5, 5)
        self.speedy = random.randint(-5, 5)

    def update(self):
        self.x += self.speedx
        self.y += self.speedy
        if self.x < 25 or self.x > 640 - 25:
            self.speedx = -self.speedx
        if self.y < 25 or self.y > 480 - 25:
            self.speedy = -self.speedy
        self.rect.center = (self.x, self.y)


# creating circle

class Circle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50, 50))

        self.image.fill((0, 255, 0))

        pygame.draw.circle(self.image, (255, 0, 0), (25, 25), 25, 0)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


def main():
    background = pygame.Surface(screen.get_size())

    # background=background.convert()https://repl.it/@eelay234/cllision-detection-circle-rect-moving-score

    background.fill((0, 255, 0))

    screen.blit(background, (0, 0))

    score = 0

    boxes = []

    for i in range(0, 20):
        boxes.append(Boxes())

    circle = Circle()

    allSprites = pygame.sprite.Group(boxes)

    circleSprite = pygame.sprite.Group(circle)

    while 1:

        for i in pygame.event.get():

            if i.type == QUIT:
                pygame.quit()
                exit()

        # checking the collision.check 'pydoc pygame.sprite.spritecollide' for mode details. True is used for sprite killing. It doesn't kill the sprite in actual.It is still present in the computer memory though.It has just removed it from the group so that no further display of that sprite is possible.

        # pygame.sprite.spritecollide(circle,allSprites,True)
        if pygame.sprite.spritecollide(circle, allSprites, True):
            score += 1
            print("collision")

        # following the CUD method
        screen.fill((0, 255, 0))

        allSprites.clear(screen, background)

        circleSprite.clear(screen, background)

        allSprites.update()

        circleSprite.update()

        allSprites.draw(screen)

        circleSprite.draw(screen)
        font = pygame.font.SysFont("Times", 30)
        text = font.render("Score: " + str(score), True, (255, 0, 255))
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.centery = 20
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()

"""You can also check the collision about the rect attributes. There are many ways to do that.Example:

1.circle.rect.colliderect(box1) will check the collision between the circle and box1 collision

2. pygame.sprite.collide_rect(sprite1,sprite2) willl also do the same """


