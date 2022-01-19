import pygame.sprite
from math import sin
from math import cos
from math import pi


class Butterfly(pygame.sprite.Sprite):
    def __init__(self, x, y, butter_body, butter_wings, direction, group):
        pygame.sprite.Sprite.__init__(self)

        self.butter_wings0 = pygame.transform.scale(butter_wings, (50, 100))
        self.butter_wings20 = pygame.transform.flip(self.butter_wings0, False, True)
        self.wings_width = self.butter_wings0.get_rect().width
        self.wings_height = self.butter_wings0.get_rect().height

        center1 = self.butter_wings0.get_rect().center
        self.butter_wings = pygame.transform.rotate(self.butter_wings0, direction - 90)
        self.wings_rect = self.butter_wings.get_rect(center=center1)
        self.butter_wings2 = pygame.transform.rotate(self.butter_wings20, direction + 90)
        self.wings_rect2 = self.butter_wings2.get_rect(center=center1)

        self.image0 = pygame.transform.scale(butter_body, (30, 100))
        self.image = self.image0
        center1 = self.image.get_rect().center
        self.image = pygame.transform.rotate(self.image, direction - 90)
        self.rect = self.image.get_rect(center=center1)
        self.x = x
        self.y = y
        self.direction = direction
        self.add(group)
        self.speed = 5

        self.alfa = 0       # ankle between horizont and a wing
        self.scale = 1

    def update(self, w1, h1, dx, dy, x0, y0, surf) -> None:
        if self.y + y0 - dy < -100 or self.y + y0 - dy > 100 + h1 - self.rect.height or \
                self.x + x0 - dx < -100 or self.x + x0 + - dx > w1 - self.rect.width + 100:
            self.kill()
        else:
            self.y -= int(self.speed * sin(self.direction*pi/180)) + dy
            self.x += int(self.speed * cos(self.direction*pi/180)) - dx

            self.image = pygame.transform.scale(self.image0, (5 + self.scale, 10 + self.scale))
            center1 = self.image.get_rect().center
            self.image = pygame.transform.rotate(self.image, self.direction - 90)
            self.rect = self.image.get_rect(center=center1)

            self.butter_wings = pygame.transform.scale(self.butter_wings0, (abs(cos(self.alfa*pi/180))*(10 + self.scale),
                                                                            10 + self.scale))
            self.alfa += 5
            self.scale += 1
            self.butter_wings2 = pygame.transform.flip(self.butter_wings, False, True)
            self.wings_width = self.butter_wings.get_rect().width
            self.wings_height = self.butter_wings.get_rect().height
            center1 = self.butter_wings.get_rect().center
            self.butter_wings = pygame.transform.rotate(self.butter_wings, self.direction - 90)
            self.wings_rect = self.butter_wings.get_rect(center=center1)
            self.butter_wings2 = pygame.transform.rotate(self.butter_wings2, self.direction + 90)
            self.wings_rect2 = self.butter_wings2.get_rect(center=center1)
        self.draw2(surf)

    def draw2(self, surf):
        surf.blit(self.image, self.image.get_rect(center=(self.x, self.y)))
        surf.blit(self.butter_wings, self.butter_wings.get_rect(center=
                                                                (self.x + 0.5*cos((self.direction-90)*pi/180)*self.wings_width,
                                                                 self.y - 0.5*sin((self.direction-90)*pi/180)*self.wings_width)))
        surf.blit(self.butter_wings2, self.butter_wings.get_rect(center=
                                                                (self.x - 0.2*cos((self.direction-90)*pi/180)*self.wings_width,
                                                                 self.y + 0.2*sin((self.direction-90)*pi/180)*self.wings_width)))