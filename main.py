from sys import exit

from obstacle import *
from board import *

from login import *
from info import Info
from coins import Coins

from PyQt5.QtWidgets import QApplication
from lyc import *




def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - sett.start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    sett.screen.blit(score_surf, score_rect)

    coin_surf = coins_font.render(f'coins: {sett.count_coins}', False, (64, 64, 64))
    coin_rect = score_surf.get_rect(center=(700, 50))
    sett.screen.blit(coin_surf, coin_rect)
    return current_time


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        sett.running = True
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




form1 = ''



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if 200 <= event.pos[0] <= 597 and 350 <= event.pos[1] <= 426:
                sett.log_in = True

        if sett.game_active:

            if sett.count_level - 1 == len(level):
                activate = False
              #  sett.count_level = 0
                sett.game_active = False
                form1.show()
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
                        form1.level.append(str(len(form1.level) + 1))

                    if obs[2] == 'no':
                        pass
                    if obs[2] == 'coin':

                        coins_group.add(Coins(coin))
                except IndexError:
                    pass

        else:
            if sett.running:
                if event.type == pike:
                    a += 1
                    if a == 2:
                        choice_enemy = r.randint(1, 2)
                        if choice_enemy == 1:
                            enemy = Enemy1()
                            DrawEnemy(enemy_sprite, enemy.get_name(), box_x + box_width // 2 - 90, 100)
                        elif choice_enemy == 2:
                            enemy = Enemy2()
                            DrawEnemy(enemy_sprite, enemy.get_name(), box_x + box_width // 2 - 90, -20)
                        spider_song.play(loops=-1)

                        enemy_text = small_font.render(f'На вас напал: {enemy.get_name()}', True, 'white')
                        big_text = big_font.render('НАЖМИТЕ [ПРОБЕЛ] ЧТО БЫ ПРИНЯТЬ БОЙ', True, 'white')

                    if enemy.get_is_attacking():
                        if choice_attack == 1:
                            enemy.attack01()
                        if choice_attack == 2:
                            enemy.attack02()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    print(pygame.mouse.get_pos())


            elif form1 == '':

                sett.screen.fill((194, 197, 170))
                sett.screen.blit(player_stand, player_stand_rect)
                    #   sett.screen.blit(button_stand, button_stand_rect)

                keys = pygame.key.get_pressed()

                score_message = test_font.render(f'Your score: {sett.score}', False, (111, 196, 169))
                score_message_rect = score_message.get_rect(center=(400, 380))
                sett.screen.blit(game_name, game_name_rect)

                if sett.score == 0:
                    sett.screen.blit(game_message, game_message_rect)
                    button = pygame.draw.rect(sett.screen, (65, 72, 51), (200, 350, 400, 80), 4)



            else:
                sett.screen.fill((194, 197, 170))
                form1.update()
                form1.show()




    if sett.log_in:
        app = QApplication(sys.argv)
        form = Login()
        sys.excepthook = except_hook
        form.show()
        sett.log_in = False
    if sett.info:
        app1 = QApplication(sys.argv)
        form1 = Info(form.name)
        form1.show()
        sett.info = False

    if sett.game_active:
        sett.screen.fill((194, 197, 170))
        heart.hp = 5
     #   sett.screen = pygame.display.set_mode((800, 600))

      #  sett.update()
        form1.hide()
        sett.screen.blit(form1.sky_surface, (0, 0))

        sett.score = display_score()
        form1.start_time = 0
        sett.game_active = collision_sprite()

        obstacle_group.draw(sett.screen)
        player.draw(sett.screen)
        board_group.draw(sett.screen)
        coins_group.draw(sett.screen)

        player.update()
        obstacle_group.update()
        board_group.update()
        coins_group.update()

        sett.screen.blit(form1.ground_surface, (0, 400))


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
     #   sett.screen = pygame.display.set_mode((1200, 800))
      #  sett.update()
        keys = pygame.key.get_pressed()
        print(keys[pygame.K_SPACE])
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_und.update('left')
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_und.update('right')
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_und.update('up')
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_und.update('down')

        if keys[pygame.K_q] and player_und_attacking:
            draw_attack_bar = True
            player_und_attacking = False
            enemy_attack_time = False
            big_text = big_font.render('НАЖМИТЕ [E] КАК МОЖНО БЛИЖЕ К ЦЕНТРУ', True, 'white')
        if keys[pygame.K_e] and draw_attack_bar:
            draw_attack_bar = False
            big_text = big_font.render('НАЖМИТЕ [ПРОБЕЛ] ЧТО БЫ ПРИНЯТЬ БОЙ', True, 'white')
            enemy_attack_time = True
            line.reset()
            damage = ((line.get_x() + 335) // 53) * 2
            if damage > 10:
                damage -= (40 - damage)
            enemy.set_hp(enemy.get_hp() - damage)
            damage_text = small_font.render(f'ВЫ НАНЕСЛИ {damage} УРОНА', True, 'white')
        if keys[pygame.K_SPACE] and not enemy.get_is_attacking() and enemy_attack_time:
            enemy.set_is_attacking(True)
            choice_attack = r.randint(1, 2)
            big_text = big_font.render('', True, 'white')
            enemy_attack_time = False
            damage_text = small_font.render(f'', True, 'white')
        if heart.get_x() < box_x:
            heart.set_x(box_x + 2)
        if heart.get_x() > box_x + box_width - heart_width:
            heart.set_x(box_x + box_width - heart_width - 2)
        if heart.get_y() < box_y:
            heart.set_y(box_y + 2)
        if heart.get_y() > box_y + box_height - heart_height:
            heart.set_y(box_y + box_height - heart_height - 2)
      #  pygame.draw.rect(sett.screen, 'white', (box_x, box_y, box_width, box_height), 0)

        ban_attack = []
        for i in attack1:
            if i.get_name() == 'peaks':
                if i.get_vector() == 'down' and i.rect.y >= 270:
                    ban_attack.append(i)
                elif i.get_vector() == 'up' and i.rect.y <= box_y:
                    ban_attack.append(i)
                elif i.get_vector() == 'right' and i.rect.x >= box_x + 170:
                    ban_attack.append(i)
                elif i.get_vector() == 'left' and i.rect.x <= box_x:
                    ban_attack.append(i)

            elif i.get_name() == 'bone':
                if i.get_vector() == 'right' and i.rect.x >= box_x + 195:
                    ban_attack.append(i)
                elif i.get_vector() == 'left' and i.rect.x <= box_x:
                    ban_attack.append(i)

            elif i.get_name() == 'ball':
                if i.get_broken() >= 15:
                    ban_attack.append(i)

            elif i.get_name() == 'block':
                if i.get_is_ban():
                    ban_attack.append(i)
                    tetris = [[0] * 10 for i in range(3)]
        for i in ban_attack:
            attack1.remove(i)

        if before_len_attack != 0 and len(attack1) == 0:
            enemy.end_attack()
            enemy.set_is_attacking(False)
            before_len_attack = 0
            big_text = big_font.render(f'НАЖМИТЕ [Q] ЧТО БЫ АТАКОВАТЬ', True, 'white')
            player_und_attacking = True

        else:
            before_len_attack = len(attack1)

        if draw_attack_bar:
            attack_bar_group.draw(sett.screen)
            line_group.update()
            line_group.draw(sett.screen)
        sett.screen.fill('black')
        enemy_hp = small_font.render(f'HP {enemy.get_name()}: {enemy.get_hp()}/20',
                                     True, 'white')
        player_und_hp = small_font.render(f'ВАШИ HP: {heart.get_hp()}', True, 'white')

        player_und.draw(sett.screen)
        attack1.draw(sett.screen)
        enemy_sprite.draw(sett.screen)
        pygame.draw.rect(sett.screen, 'white', (box_x, box_y, box_width, box_height), 2)
        heart.heat()

        attack1.update()
        enemy_sprite.update()

        sett.screen.blit(enemy_text, (50, 50))
        sett.screen.blit(big_text, (100, 700))
        sett.screen.blit(damage_text, (470, 520))
        sett.screen.blit(enemy_hp, (730, 310))
        sett.screen.blit(player_und_hp, (730, 480))

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
