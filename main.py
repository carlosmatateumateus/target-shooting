import pygame
from sys import exit
from pygame.locals import *
from random import randint

WINDOW_SIZE = (1024, 576)

window = pygame.display.set_mode(WINDOW_SIZE)
window_color = [255, 255, 255]

pygame.init()
pygame.display.set_caption('target-shooting')

my_font = pygame.font.SysFont('Fira Code', 14)
my_font_alert = pygame.font.SysFont('Fira Code', 40)

pygame.mouse.set_visible(False)

pato = pygame.transform.scale(pygame.image.load('assets/pato.png'), [100, 100])
sniper = pygame.transform.scale(pygame.image.load('assets/sniper.png'), [70, 70])

hit = pygame.mixer.Sound('assets/hit.wav')

seconds_on_game = 0


def game():

    lose = False
    winner = False

    first_enemie_x = randint(500, 1024)
    second_enemie_x = randint(500, 1024)
    third_enemie_x = randint(500, 1024)

    score = 0
    failure = 0

    mouse_color = [99, 83, 53]

    global display
    global window_color
    global seconds_on_game 

    velocity = 2.7

    winner_label = my_font_alert.render('You are winner!', True, 'white')
    loser_label = my_font_alert.render('You are loser!', True, 'white')

    press_caution = my_font.render('Prima espaço para continuar ...', True, [255, 255, 255])
    while True:
        seconds_on_game += 1

        if seconds_on_game > 2500:
            velocity += 0.2
            seconds_on_game = 0
        
        label_ponts = my_font.render('Ponts', True, 'black')
        ponts = my_font.render(f'{score}', True, 'white')

        label_flaws = my_font.render('Failure', True, 'black')
        flaws = my_font.render(f'{failure}', True, 'white')

        window.fill(window_color)

        for event in pygame.event.get():  # Get all events. Example: Mouse move, keyboard pressed.
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:

                if mouse_move.colliderect(first_enemie):
                    first_enemie_x = 1024
                    score += 1
                    hit.play()

                if mouse_move.colliderect(second_enemie):
                    second_enemie_x = 1024
                    score += 1
                    hit.play()

                if mouse_move.colliderect(third_enemie):
                    third_enemie_x = 1024
                    score += 1
                    hit.play()

        if (winner == False) and (lose == False):
            pygame.draw.rect(window, '#000000', [0, 341/2, 1024, 5])
            pygame.draw.rect(window, '#000000', [0, 682/2, 1024, 5])
            pygame.draw.rect(window, '#000000', [0, 1023/2, 1024, 5])

            pygame.draw.rect(window, [200, 200, 200], [20, 15, 120, 40], border_radius=4)
            pygame.draw.rect(window, [57, 167, 63], [80, 20, 50, 30], border_radius=4)

            pygame.draw.rect(window, [200, 200, 200], [180, 15, 150, 40], border_radius=4)
            pygame.draw.rect(window, [223, 56, 26], [270, 20, 50, 30], border_radius=4)


            first_enemie = pygame.Rect(first_enemie_x, 341/2- 100, 100, 100)
            second_enemie = pygame.Rect(second_enemie_x, 682/2 - 100, 100, 100)
            third_enemie = pygame.Rect(third_enemie_x, 1023/2 - 100, 100, 100)


            first_enemie_x -= velocity
            second_enemie_x -= velocity
            third_enemie_x -= velocity


            if first_enemie_x < -100:
                first_enemie_x = 1024
                failure += 1
                
            if second_enemie_x < -100:
                second_enemie_x = 1024
                failure += 1

            if third_enemie_x < -100:
                third_enemie_x = 1024
                failure += 1
            
            window.blit(label_ponts, [25, 25])
            window.blit(ponts, [100, 25])

            window.blit(label_flaws, [185, 25])
            window.blit(flaws, [290, 25])

            window.blit(pato, [first_enemie.x, first_enemie.y])
            window.blit(pato, [second_enemie.x, second_enemie.y])
            window.blit(pato, [third_enemie.x, third_enemie.y])

            mouse_move = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 19, 19)
            
        if score == 150:
            winner = True
            window_color = [57, 167, 63]
            window.blit(winner_label, [355, 250])
            window.blit(press_caution, [400, 320])
            if pygame.key.get_pressed()[K_SPACE]:
                winner = False
                failure = 0
                score = 0
                velocity = 2.7
                seconds_on_game = 0
                window_color = 'white'
        if failure == 150:
            lose = True
            window_color = [223, 56, 26]
            window.blit(loser_label, [355, 250])
            window.blit(press_caution, [400, 320])
            if pygame.key.get_pressed()[K_SPACE]:
                lose = False
                failure = 0
                score = 0
                velocity = 2.7
                seconds_on_game = 0
                window_color = 'white'

        window.blit(sniper, [pygame.mouse.get_pos()[0] - 70/2, pygame.mouse.get_pos()[1] - 70/2])
        pygame.display.flip()

game()