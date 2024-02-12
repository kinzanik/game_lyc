from sys import exit

from obstacle import *
from board import *

from login import *
from info import Info
from coins import Coins

from PyQt5.QtWidgets import QApplication
from lyc import *
import undertale

from would_u import WouldYou




def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - sett.start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(600, 50))
    sett.screen.blit(score_surf, score_rect)

    coin_surf = coins_font.render(f'coins: {sett.count_coins}', False, (64, 64, 64))
    coin_rect = score_surf.get_rect(center=(900, 50))
    sett.screen.blit(coin_surf, coin_rect)
    return current_time


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        if sett.first_would == 0:
            sett.would = True
            sett.first_would += 1
        else:
            sett.form2.show()
            sett.perehod = True

        obstacle_group.empty()
        board_group.empty()
        board_up_group.empty()
        coins_group.empty()
        return False
    if pygame.sprite.spritecollide(player.sprite, coins_group, False):
        coins_group.empty()
        sett.count_coins += 1
        return True

    elif pygame.sprite.spritecollide(player.sprite, board_group, False):
            sett.pl.update_board()
            return True
    elif pygame.sprite.spritecollide(player.sprite, board_up_group, False):
        sett.pl.update_board_up()
        return True
    else:
        return True




sett.form1 = 'l'



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if sett.form1 == 'l':
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if 401 <= event.pos[0] <= 818 and 350 <= event.pos[1] <= 425:
                    if sett.form == '':
                        sett.log_in = True
                    else:
                        sett.form.show()

        if sett.game_active:

            if sett.count_level - 1 == len(level):
                activate = False
              #  sett.count_level = 0
                sett.game_active = False
                sett.form1.show()
                obstacle_group.empty()
                board_group.empty()
            if event.type == obstacle_timer:
                sett.count_level += 1
                try:
                    obs = sett.level[sett.count_level - 1].split(',')
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
                    if obs[0] == 'wol':
                        obstacle_group.add(Obstacle(wolf))
                    if obs[0] == 'pig':
                        obstacle_group.add(Obstacle(pig))
                    if obs[0] == 'hor':
                        obstacle_group.add(Obstacle(horse))
                    if obs[0] == 'f':
                        pass
                    if obs[1] == '-':
                        ex = Board(grass)
                        board_group.add(ex)
                    if obs[1] == '--':
                        ex = Board(board)
                        board_group.add(ex)
                    if obs[1] == 'f':
                        sett.form1.level.append(str(len(sett.form1.level) + 1))

                    if obs[2] == 'no':
                        pass
                    if obs[2] == 'coin':

                        coins_group.add(Coins(coin))
                except IndexError:
                    pass


        elif sett.form1 == 'l':
            print(sett.form1)

            sett.screen.fill((194, 197, 170))
            sett.screen.blit(player_stand, player_stand_rect)
                    #   sett.screen.blit(button_stand, button_stand_rect)

            keys = pygame.key.get_pressed()

            score_message = test_font.render(f'Your score: {sett.score}', False, (111, 196, 169))
            score_message_rect = score_message.get_rect(center=(400, 380))
            sett.screen.blit(game_name, game_name_rect)

            if sett.score == 0:
                sett.screen.blit(game_message, game_message_rect)
                button = pygame.draw.rect(sett.screen, (65, 72, 51), (400, 350, 420, 80), 4)


        elif sett.perehod:
            sett.screen.fill((194, 197, 170))
            sett.form1.hide()
        else:
            sett.screen.fill((194, 197, 170))
            sett.form1.update()
            if not sett.perehod:
                sett.form1.show()




    if sett.log_in:
        app = QApplication(sys.argv)
        sett.form = Login()
        sys.excepthook = except_hook
        sett.form.show()
        sett.log_in = False
    if sett.info:
        app1 = QApplication(sys.argv)
        sett.form1 = Info(sett.form.name)
        sett.form1.show()
        sett.info = False

    if sett.would:
        sett.form1.hide()
        app2 = QApplication(sys.argv)
        sett.form2 = WouldYou()
        sett.form2.show()
        sett.would = False
        sett.perehod = True

    if sett.game_active:
        sett.screen.fill((194, 197, 170))

     #   sett.screen = pygame.display.set_mode((800, 600))

      #  sett.update()
        sett.form1.hide()
        sett.screen.blit(sett.form1.sky_surface, (0, 0))

        sett.score = display_score()
        sett.form1.start_time = 0
        sett.game_active = collision_sprite()

        obstacle_group.draw(sett.screen)
        player.draw(sett.screen)
        board_group.draw(sett.screen)
        coins_group.draw(sett.screen)

        player.update()
        obstacle_group.update()
        board_group.update()
        coins_group.update()

        sett.screen.blit(sett.form1.ground_surface, (0, 600))


        pink_girl.update()
        green_girl.update()
        fairy.update()
        bat.update()
        bat_high.update()
        bird.update()
        white_bird.update()
        lower_bird.update()
        wolf.update()
        pig.update()
        horse.update()

        coin.update()

    if sett.running:
        a = undertale.under()





    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
