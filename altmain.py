# import pygame
# import random
# import sys
# import os

# pygame.init()

# clock = pygame.time.Clock()
# fps = 60

# screen_width = 864
# screen_height = 936

# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Flappy Bird')

# #define font
# font = pygame.font.SysFont('Bauhaus 93', 60)

# #define colours
# white = (255, 255, 255)

# #define game variables
# ground_scroll = 0
# scroll_speed = 4
# flying = False
# game_over = False
# pipe_gap = 150
# pipe_frequency = 1500 #milliseconds
# last_pipe = pygame.time.get_ticks() - pipe_frequency
# score = 0
# pass_pipe = False

# current_directory = os.getcwd()
# #pygame.image.load(current_directory + "\hamburger.jpg").convert()
# #load images
# bg = pygame.image.load(os.path.join(current_directory, 'imgs', 'kg.png'))
# ground_img = pygame.image.load(os.path.join(current_directory, 'imgs', 'ground.png'))
# button_img = pygame.image.load(os.path.join(current_directory, 'imgs', 'load.png'))


# def draw_text(text, font, text_col, x, y, surface):
#     img = font.render(text, True, text_col)
#     surface.blit(img, (x, y))


# def reset_game(pipe_group, flappy, screen_width, screen_height):
#     pipe_group.empty()
#     flappy.rect.x = 100
#     flappy.rect.y = int(screen_height / 2)
#     score = 0
#     return score


# class Bird(pygame.sprite.Sprite):
#     def __init__(self, x, y, image_paths):
#         pygame.sprite.Sprite.__init__(self)
#         self.images = []
#         self.index = 0
#         self.counter = 0
#         for path in image_paths:
#             img = pygame.image.load(path)
#             self.images.append(img)
#         self.image = self.images[self.index]
#         self.rect = self.image.get_rect()
#         self.rect.center = [x, y]
#         self.vel = 0
#         self.clicked = False
#     def update(self, max_height):
#         if flying:
#             #gravity
#             self.vel += 0.5
#             if self.vel > 8:
#                 self.vel = 8
#             if self.rect.bottom < max_height:
#                 self.rect.y += int(self.vel)
#         if not game_over:
#             #jump
#             mouse_pressed = pygame.mouse.get_pressed()[0]
#             if mouse_pressed == 1 and not self.clicked:
#                 self.clicked = True
#                 self.vel = -10
#             if mouse_pressed == 0:
#                 self.clicked = False

#             #handle the animation
#             self.counter += 1
#             flap_cooldown = 5

#             if self.counter > flap_cooldown:
#                 self.counter = 0
#                 self.index += 1
#                 if self.index >= len(self.images):
#                     self.index = 0
#             self.image = self.images[self.index]

#             #rotate the bird
#             self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
#         else:
#             self.image = pygame.transform.rotate(self.images[self.index], -90)

# class Pipe(pygame.sprite.Sprite):
#     def __init__(self, x, y, position):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(os.path.join(current_directory, 'imgs', 'pipe.png'))
#         self.rect = self.image.get_rect()
#         #position 1 is from the top, -1 is from the bottom
#         if position == 1:
#             self.image = pygame.transform.flip(self.image, False, True)
#             self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
#         if position == -1:
#             self.rect.topleft = [x, y + int(pipe_gap / 2)]

#     def update(self):
#         self.rect.x -= scroll_speed
#         if self.rect.right < 0:
#             self.kill()


# class Button():
#     def __init__(self, x, y, image):
#         self.image = image
#         self.rect = self.image.get_rect(topleft=(x, y))

#     def is_clicked(self):
#         pos = pygame.mouse.get_pos()
#         if self.rect.collidepoint(pos):
#             if pygame.mouse.get_pressed()[0] == 1:
#                 return True
#         return False

#     def draw(self):
#         screen.blit(self.image, self.rect)


# bird_group = pygame.sprite.Group()
# pipe_group = pygame.sprite.Group()

# flappy = Bird(100, int(screen_height / 2))

# bird_group.add(flappy)

# #create restart button instance
# button = Button(screen_width // 2 - 50, screen_height // 2 - 100, button_img)

# run = True
# while run:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if button.rect.collidepoint(event.pos):
#                 reset_game()

#     clock.tick(fps)

#     #draw background
#     screen.blit(bg, (0,0))

#     bird_group.draw(screen)
#     bird_group.update()
#     pipe_group.draw(screen)

#     #draw the ground
#     screen.blit(ground_img, (ground_scroll, 768))

#     #check the score
#     if len(pipe_group) > 0:
#         if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
#             and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
#             and pass_pipe == False:
#             pass_pipe = True
#         if pass_pipe == True:
#             if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
#                 score += 1
#                 pass_pipe = False

#     if game_over == True:
#         if button.draw() == True:
#             reset_game()

#     pygame.display.update()

# pygame.quit()
# sys.exit()

import pygame
from pygame.locals import *
import random
import sys
import os

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

#define font
font = pygame.font.SysFont('Bauhaus 93', 60)

#define colours
white = (255, 255, 255)

#define game variables
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 1500 #milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

current_directory = os.getcwd()
#pygame.image.load(current_directory + "\hamburger.jpg").convert()
#load images
bg = pygame.image.load(os.path.join(current_directory, 'imgs', 'kg.png'))
ground_img = pygame.image.load(os.path.join(current_directory, 'imgs', 'ground.png'))
button_img = pygame.image.load(os.path.join(current_directory, 'imgs', 'load.png'))


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_height / 2)
    score = 0
    return score


#f'img/bird{num}.png'
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(os.path.join(current_directory, 'imgs', f'sprite{num}.png'))
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):

        if flying == True:
            #gravity
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        if game_over == False:
            #jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            #handle the animation
            self.counter += 1
            flap_cooldown = 5

            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            #rotate the bird
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)



class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(current_directory, 'imgs', 'pipe.png'))
        self.rect = self.image.get_rect()
        #position 1 is from the top, -
        button.draw()
        if button.draw():
            game_over = False
            score = reset_game()

pygame.display.update()



    
