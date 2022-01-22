import pygame.sprite
from math import sin
from math import pi


class Hero:
    def __init__(self, x, y, speed, surf, W, H, W2, H2, surf_head, surf_head_down, surf_tail,
                 surf_leg_a_a, surf_leg_a_b, surf_leg_down):
        self.image = surf
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.W = W
        self.H = H
        self.W2 = W2
        self.H2 = H2

        self.hero_up = surf
        self.hero_down = surf
        self.hero_left = pygame.transform.rotate(surf, -5)
        self.hero_right = pygame.transform.rotate(surf, 5)
        self.hero_surf = self.hero_left

        self.head_left = surf_head
        self.head_right = pygame.transform.flip(surf_head, True, False)
        self.head_down = surf_head_down
        self.head_up = pygame.transform.flip(self.head_down, False, True)
        self.head = self.head_left
        self.x_head = x - 50
        self.y_head = y + 5

        self.tail_left = surf_tail
        self.tail_right = pygame.transform.flip(surf_tail, True, False)
        self.tail_down = pygame.transform.rotate(surf_tail, 90)
        self.tail_up = pygame.transform.rotate(surf_tail, -90)
        self.tail = self.tail_left
        self.x_tail = x + 40
        self.y_tail = y + 5

        self.leg_a_a_left = surf_leg_a_a
        self.leg_a_a_right = pygame.transform.flip(surf_leg_a_a, True, False)
        self.leg_a_a = self.leg_a_a_left
        self.x_leg_a_a = x - 40
        self.y_leg_a_a = y + 20

        self.leg_a_b_left = surf_leg_a_b
        self.leg_a_b_right = pygame.transform.flip(surf_leg_a_b, True, False)
        self.leg_a_b = self.leg_a_b_left
        self.x_leg_a_b = x + 20
        self.y_leg_a_b = y + 20

        self.leg_down = surf_leg_down

        self.iter1 = 0
        self.iter2 = 0

    def update1(self, bt, x2, y2) -> None:
        if self.iter1 <= 30:
            self.y_head += .1
            if self.tail == self.tail_left or self.tail == self.tail_right:
                self.y_tail += .2
            else:
                self.x_tail += .2
            self.iter1 += 1
        elif 30 < self.iter1 <= 61:
            self.y_head -= .1
            if self.tail == self.tail_left or self.tail == self.tail_right:
                self.y_tail -= .2
            else:
                self.x_tail -= .2
            self.iter1 += 1
        else:
            self.iter1 = 0
        if bt[pygame.K_LEFT]:
            if self.head != self.head_left:
                self.iter2 = 0
                self.head = self.head_left
                self.x_head = self.rect.x - 0
                self.y_head = self.rect.y + 55

                self.tail = self.tail_left
                self.x_tail = self.rect.x + 85
                self.y_tail = self.rect.y + 55

                self.x_leg_a_a = self.rect.x - 5
                self.y_leg_a_a = self.rect.y + 70
                self.leg_a_a = self.leg_a_a_left

                self.x_leg_a_b = self.rect.x + 65
                self.y_leg_a_b = self.rect.y + 70
                self.leg_a_b = self.leg_a_b_left

                self.hero_surf = self.hero_left
            if self.rect.x > 3 / 8 * self.W - self.rect.width:
                self.rect.x -= self.speed
                self.x_head -= self.speed
                self.x_tail -= self.speed
                if self.iter2 <= 5:
                    self.x_leg_a_a -= 0
                    self.x_leg_a_b -= 2*self.speed
                    self.y_leg_a_b -= 1
                    self.iter2 += 1
                elif 5 < self.iter2 <= 11:
                    self.x_leg_a_a -= 2 * self.speed
                    self.x_leg_a_b -= 0
                    self.y_leg_a_a -= 1
                    self.iter2 += 1
                else:
                    self.iter2 = 0
                    self.y_leg_a_a += 6
                    self.y_leg_a_b += 6
            elif self.rect.x + x2 + self.rect.width > 230:
                x2 -= self.speed
                if self.iter2 <= 5:
                    self.x_leg_a_a += self.speed
                    self.x_leg_a_b -= self.speed
                    self.y_leg_a_b -= 1
                    self.iter2 += 1
                elif 5 < self.iter2 <= 11:
                    self.x_leg_a_a -= self.speed
                    self.x_leg_a_b += self.speed
                    self.y_leg_a_a -= 1
                    self.iter2 += 1
                else:
                    self.iter2 = 0
                    self.y_leg_a_a += 6
                    self.y_leg_a_b += 6
            else:
                self.rect.x = 3 / 8 * self.W - self.rect.width
        elif bt[pygame.K_RIGHT]:
            if self.head != self.head_right:
                self.iter2 = 0
                self.head = self.head_right
                self.x_head = self.rect.x + 80
                self.y_head = self.rect.y + 55

                self.tail = self.tail_right
                self.x_tail = self.rect.x - 20
                self.y_tail = self.rect.y + 55

                self.x_leg_a_a = self.rect.x + 85
                self.y_leg_a_a = self.rect.y + 65
                self.leg_a_a = self.leg_a_a_right

                self.x_leg_a_b = self.rect.x + 5
                self.y_leg_a_b = self.rect.y + 65
                self.leg_a_b = self.leg_a_b_right

                self.hero_surf = self.hero_right
            if self.rect.x < 5 / 8 * self.W:
                self.rect.x += self.speed
                self.x_head += self.speed
                self.x_tail += self.speed
                if self.iter2 <= 5:
                    self.x_leg_a_a -= 0
                    self.x_leg_a_b += 2*self.speed
                    self.y_leg_a_b -= 1
                    self.iter2 += 1
                elif 5 < self.iter2 <= 11:
                    self.x_leg_a_a += 2 * self.speed
                    self.x_leg_a_b += 0
                    self.y_leg_a_a -= 1
                    self.iter2 += 1
                else:
                    self.iter2 = 0
                    self.y_leg_a_a += 6
                    self.y_leg_a_b += 6
            elif self.rect.x + x2 < self.W2 - self.rect.width - 120:
                x2 += self.speed
                if self.iter2 <= 5:
                    self.x_leg_a_a -= self.speed
                    self.x_leg_a_b += self.speed
                    self.y_leg_a_b -= 1
                    self.iter2 += 1
                elif 5 < self.iter2 <= 11:
                    self.x_leg_a_a += self.speed
                    self.x_leg_a_b -= self.speed
                    self.y_leg_a_a -= 1
                    self.iter2 += 1
                else:
                    self.iter2 = 0
                    self.y_leg_a_a += 6
                    self.y_leg_a_b += 6
            else:
                self.rect.x = 5 / 8 * self.W
        elif bt[pygame.K_UP]:
            if self.head != self.head_up:
                self.hero_surf = self.hero_up
                self.head = self.head_up
                self.x_head = self.rect.x + 30
                self.y_head = self.rect.y + 15

                self.tail = self.tail_up
                self.x_tail = self.rect.x + 40
                self.y_tail = self.rect.y + 65

                self.leg_a_a = self.leg_down
                self.leg_a_b = self.leg_down
                self.x_leg_a_a = self.rect.x + 28
                self.y_leg_a_a = self.rect.y + 30
                self.x_leg_a_b = self.rect.x + 62
                self.y_leg_a_b = self.rect.y + 50

                self.iter2 = 0

            if self.rect.y > 3 / 8 * self.H - self.rect.height:
                self.rect.y -= self.speed
                self.y_head -= self.speed
                self.y_tail -= self.speed
                if self.iter2 <= 5:
                    self.y_leg_a_a -= 0
                    self.y_leg_a_b -= 2 * self.speed
                    self.iter2 += 1
                elif 5 < self.iter2 <= 11:
                    self.y_leg_a_a -= 2 * self.speed
                    self.y_leg_a_b -= 0
                    self.iter2 += 1
                else:
                    self.iter2 = 0
            elif self.rect.y + y2 + self.rect.height > 150:
                y2 -= self.speed
                if self.iter2 <= 5:
                    self.y_leg_a_a += self.speed
                    self.y_leg_a_b -= self.speed
                    self.iter2 += 1
                elif 5 < self.iter2 <= 11:
                    self.y_leg_a_a -= self.speed
                    self.y_leg_a_b += self.speed
                    self.iter2 += 1
                else:
                    self.iter2 = 0
            else:
                self.rect.y = 3 / 8 * self.H - self.rect.height
        elif bt[pygame.K_DOWN]:
            if self.head != self.head_down:
                self.head = self.head_down
                self.x_head = self.rect.x + 35
                self.y_head = self.rect.y + 68

                self.tail = self.tail_down
                self.x_tail = self.rect.x + 40
                self.y_tail = self.rect.y

                self.leg_a_a = self.leg_down
                self.leg_a_b = self.leg_down
                self.x_leg_a_a = self.rect.x + 28
                self.y_leg_a_a = self.rect.y + 70
                self.x_leg_a_b = self.rect.x + 62
                self.y_leg_a_b = self.rect.y + 45
                self.hero_surf = self.hero_down

                self.iter2 = 0

            if self.rect.y < 5 / 8 * self.H:
                self.rect.y += self.speed
                self.y_head += self.speed
                self.y_tail += self.speed
                if self.iter2 <= 5:
                    self.y_leg_a_a -= 0
                    self.y_leg_a_b += 2 * self.speed
                    self.iter2 += 1
                elif 5 < self.iter2 <= 11:
                    self.y_leg_a_a += 2 * self.speed
                    self.y_leg_a_b -= 0
                    self.iter2 += 1
                else:
                    self.iter2 = 0
            elif self.rect.y + y2 < self.H2 - 160:
                y2 += self.speed
                if self.iter2 <= 5:
                    self.y_leg_a_a -= self.speed
                    self.y_leg_a_b += self.speed
                    self.iter2 += 1
                elif 5 < self.iter2 <= 11:
                    self.y_leg_a_a += self.speed
                    self.y_leg_a_b -= self.speed
                    self.iter2 += 1
                else:
                    self.iter2 = 0
            else:
                self.rect.y = 5 / 8 * self.H
        return x2, y2

    def draw2(self, surf1):
        surf1.blit(self.leg_a_b, (self.x_leg_a_b, self.y_leg_a_b))
        surf1.blit(self.leg_a_a, (self.x_leg_a_a, self.y_leg_a_a))
        surf1.blit(self.tail, (self.x_tail, self.y_tail))
        surf1.blit(self.head, (self.x_head, self.y_head))
        surf1.blit(self.hero_surf, (self.rect.x, self.rect.y))