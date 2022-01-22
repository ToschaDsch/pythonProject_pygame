import pygame.sprite


class Hero:
    def __init__(self, x, y, speed, surf, W, H, W2, H2, surf_head, surf_head_down, surf_tail):
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

        self.iter1 = 0

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
        print("iter=", self.iter1)
        print(self.y_head)
        if bt[pygame.K_LEFT]:
            if self.head != self.head_left:
                self.head = self.head_left
                self.x_head = self.rect.x - 0
                self.y_head = self.rect.y + 55

                self.tail = self.tail_left
                self.x_tail = self.rect.x + 85
                self.y_tail = self.rect.y + 55

                self.hero_surf = self.hero_left
            if self.rect.x > 3 / 8 * self.W - self.rect.width:
                self.rect.x -= self.speed
                self.x_head -= self.speed
                self.x_tail -= self.speed
            elif self.rect.x + x2 + self.rect.width > 230:
                x2 -= self.speed
            else:
                self.rect.x = 3 / 8 * self.W - self.rect.width
        elif bt[pygame.K_RIGHT]:
            if self.head != self.head_right:
                self.head = self.head_right
                self.x_head = self.rect.x + 75
                self.y_head = self.rect.y + 55

                self.tail = self.tail_right
                self.x_tail = self.rect.x - 20
                self.y_tail = self.rect.y + 55

                self.hero_surf = self.hero_right
            if self.rect.x < 5 / 8 * self.W:
                self.rect.x += self.speed
                self.x_head += self.speed
                self.x_tail += self.speed
            elif self.rect.x + x2 < self.W2 - self.rect.width - 120:
                x2 += self.speed
            else:
                self.rect.x = 5 / 8 * self.W
        elif bt[pygame.K_UP]:
            self.hero_surf = self.hero_up
            self.x_head = self.rect.x + 20
            self.y_head = self.rect.y + 20

            self.tail = self.tail_up
            self.x_tail = self.rect.x + 40
            self.y_tail = self.rect.y + 65

            if self.rect.y > 3 / 8 * self.H - self.rect.height:
                self.rect.y -= self.speed
                self.y_head -= self.speed
                self.y_tail -= self.speed
            elif self.rect.y + y2 + self.rect.height > 150:
                y2 -= self.speed
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

                self.hero_surf = self.hero_down

            if self.rect.y < 5 / 8 * self.H:
                self.rect.y += self.speed
                self.y_head += self.speed
                self.y_tail += self.speed
            elif self.rect.y + y2 < self.H2 - 160:
                y2 += self.speed
            else:
                self.rect.y = 5 / 8 * self.H
        return x2, y2

    def draw2(self, surf1):
        surf1.blit(self.tail, (self.x_tail, self.y_tail))
        surf1.blit(self.head, (self.x_head, self.y_head))
        surf1.blit(self.hero_surf, (self.rect.x, self.rect.y))