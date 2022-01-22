import pygame.sprite
from math import sin
from math import cos
from math import pi


class Butterfly(pygame.sprite.Sprite):
    def __init__(self, x, y, butter_body, butter_wings, direction, group):
        pygame.sprite.Sprite.__init__(self)

        self.butter_wings0 = butter_wings
        self.butter_wings20 = pygame.transform.flip(self.butter_wings0, False, True)
        self.wings_width = self.butter_wings0.get_rect().width
        self.wings_height = self.butter_wings0.get_rect().height

        center1 = self.butter_wings0.get_rect().center
        self.butter_wings = pygame.transform.rotate(self.butter_wings0, direction - 90)
        self.wings_rect = self.butter_wings.get_rect(center=center1)
        self.butter_wings2 = pygame.transform.rotate(self.butter_wings20, direction + 90)
        self.wings_rect2 = self.butter_wings2.get_rect(center=center1)

        self.image0 = butter_body
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
        if self.y + y0 - dy < -500 or self.y + y0 - dy > 500 + h1 - self.rect.height or \
                self.x + x0 - dx < -500 or self.x + x0 + - dx > w1 - self.rect.width + 500:
            self.kill()
        else:
            self.y -= int(self.speed * sin(self.direction*pi/180)) + dy
            self.x += int(self.speed * cos(self.direction*pi/180)) - dx

            scale_x = 5 * (1 + self.scale)
            scale_y = 25 * (1 + self.scale)
            self.image = pygame.transform.scale(self.image0, (scale_x, scale_y))
            center1 = self.image.get_rect().center
            self.image = pygame.transform.rotate(self.image, self.direction - 90)
            self.rect = self.image.get_rect(center=center1)

            scale_x = 12.5 * (1 + self.scale)*abs(cos(self.alfa*pi/180))
            scale_y = 25 * (1 + self.scale)
            self.butter_wings = pygame.transform.scale(self.butter_wings0, (scale_x, scale_y))

            self.butter_wings2 = pygame.transform.flip(self.butter_wings, False, True)
            self.wings_width = self.butter_wings.get_rect().width
            self.wings_height = self.butter_wings.get_rect().height
            center1 = self.butter_wings.get_rect().center
            self.butter_wings = pygame.transform.rotate(self.butter_wings, self.direction - 90)
            self.wings_rect = self.butter_wings.get_rect(center=center1)
            self.butter_wings2 = pygame.transform.rotate(self.butter_wings2, self.direction + 90)
            self.wings_rect2 = self.butter_wings2.get_rect(center=center1)
            self.alfa += 5
            self.scale += 0.05
        self.draw2(surf)

    def draw2(self, surf):
        surf.blit(self.image, self.image.get_rect(center=(self.x, self.y)))
        surf.blit(self.butter_wings,
                  self.butter_wings.get_rect(center=
                                            (self.x + 0.55*cos((self.direction-90)*pi/180)*self.wings_width,
                                            self.y - 0.55*sin((self.direction-90)*pi/180)*self.wings_width)))
        surf.blit(self.butter_wings2,
                  self.butter_wings.get_rect(center=
                                            (self.x - 0.55*cos((self.direction-90)*pi/180)*self.wings_width,
                                            self.y + 0.55*sin((self.direction-90)*pi/180)*self.wings_width)))