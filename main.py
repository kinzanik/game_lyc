from sys import exit
from random import choice
from player import *
from obstacle import *
from board import *
from boardup import *
from sprites import *
from load_image import load_image
from bool import sett
from settings import *
from login import *
from info import Info
from PyQt5.QtCore import Qt, QPoint
from math import cos, sin, pi
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - sett.start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        board_group.empty()
        board_up_group.empty()

        return False
    elif pygame.sprite.spritecollide(player.sprite, board_group, False):
        #  pl.rect = pl.image.get_rect(midbottom=(200, 210))
            sett.pl.update_board()
            return True
    elif pygame.sprite.spritecollide(player.sprite, board_up_group, False):
        #  pl.rect = pl.image.get_rect(midbottom=(200, 210))
        sett.pl.update_board_up()
        return True
    else:
        return True




form1 = ''



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if sett.game_active:
            if sett.count_level - 1 == len(level):
                activate = False
                sett.count_level = 0
                sett.game_active = False
                form1.show()
                obstacle_group.empty()
                board_group.empty()
            if event.type == obstacle_timer:
                sett.count_level += 1
                try:
                    obs = level[sett.count_level - 1].split(',')
                    print(obs)
                    if obs[0] == 'vv':
                        obstacle_group.add(Obstacle(bat))
                    if obs[0] == 'v':
                        obstacle_group.add(Obstacle(bat_high))
                    if obs[0] == 'b':
                        obstacle_group.add(Obstacle(bird))
                    if obs[0] == 'lb':
                        obstacle_group.add(Obstacle(lower_bird))
                    if obs[0] == 'w':
                        obstacle_group.add(Obstacle(white_bird))

                    if obs[0] == 'f':
                        pass
                    if obs[1] == '-':
                        ex = Board(grass)
                        board_group.add(ex)
                    if obs[1] == '--':
                        ex = Board(board)
                        board_group.add(ex)
                    if obs[1] == 'f':
                        pass
                except IndexError:
                    pass

                #     elif event.type == board_timer:


            #    else:
                  #  board_up_group.add(BoardUp(choice(['board', 'board', ''])))

        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if 200 <= event.pos[0] <= 597 and 350 <= event.pos[1] <= 426:
                    sett.log_in = True

    if sett.log_in:
        app = QApplication(sys.argv)
        form = Login()
        sys.excepthook = except_hook
        form.show()
        sett.log_in = False
        # info = True
#    print(sett.info)
    if sett.info:
        app1 = QApplication(sys.argv)
        form1 = Info(form.name)
        form1.show()
        sett.info = False

    if sett.game_active:
        form1.hide()
        screen.blit(sky_surface, (0, 0))

        sett.score = display_score()
        form1.start_time = 0
        sett.game_active = collision_sprite()

        obstacle_group.draw(screen)
        player.draw(screen)
        board_group.draw(screen)


        player.update()
        obstacle_group.update()
        board_group.update()

        screen.blit(ground_surface, (0, 400))

      #  board_up_group.draw(screen)
        #board_up_group.update()

  #      sett.game_active = collision_sprite()


        pink_girl.update()
        green_girl.update()
        fairy.update()
        bat.update()
        bat_high.update()
        bird.update()
        white_bird.update()
        lower_bird.update()




    else:
        if form1 == '':
            screen.fill((194, 197, 170))
            screen.blit(player_stand, player_stand_rect)
            #   screen.blit(button_stand, button_stand_rect)

            keys = pygame.key.get_pressed()


            score_message = test_font.render(f'Your score: {sett.score}', False, (111, 196, 169))
            score_message_rect = score_message.get_rect(center=(400, 380))
            screen.blit(game_name, game_name_rect)

            if sett.score == 0:
                screen.blit(game_message, game_message_rect)
                button = pygame.draw.rect(screen, (65, 72, 51), (200, 350, 400, 80), 4)

            else:
                screen.blit(score_message, score_message_rect)
        else:
            form1.update()
            form1.show()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
