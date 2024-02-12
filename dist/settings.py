import pygame
from load_image import load_image
from sprites import AnimatedSprite
from bool import sett



pygame.init()

pygame.display.set_caption("forest's secrets")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/EightBits.ttf', 50)
coins_font = pygame.font.Font('font/EightBits.ttf', 40)
#bg_music = pygame.mixer.Sound('music/menu_music.mp3')
#bg_music.play(loops=-1)
# Groups
player = pygame.sprite.GroupSingle()


obstacle_group = pygame.sprite.Group()
board_group = pygame.sprite.Group()
board_up_group = pygame.sprite.Group()
coins_group = pygame.sprite.Group()


# Intro screen
fairy = AnimatedSprite(load_image("graphics/player/1.png"), 5, 1, 50, 50, player)
fairy_jump = AnimatedSprite(load_image("graphics/player/2.png"), 5, 1, 50, 50, player)
first_skin = [fairy, fairy_jump]

pink_girl = AnimatedSprite(load_image("graphics/player1/1.png"), 4, 1, 50, 50, player)
pink_girl_jump = AnimatedSprite(load_image("graphics/player1/2.png"), 4, 1, 50, 50, player)
second_skin = [pink_girl, pink_girl_jump]

green_girl = AnimatedSprite(load_image("graphics/player2/1.png"), 4, 1, 50, 50, player)
green_girl_jump = AnimatedSprite(load_image("graphics/player2/2.png"), 4, 1, 50, 50, player)
third_skin = [green_girl, green_girl_jump]

bat = AnimatedSprite(load_image('graphics/damage/Bat.png'), 1, 15, 50, 50, obstacle_group)
bat_high = AnimatedSprite(load_image('graphics/damage/Bat.png'), 1, 15, 50, 50, obstacle_group)

bird = AnimatedSprite(load_image('graphics/damage/bird.png'), 3, 1, 50, 50, obstacle_group)
lower_bird = AnimatedSprite(load_image('graphics/damage/bird.png'), 3, 1, 50, 50, obstacle_group)

white_bird = AnimatedSprite(load_image('graphics/damage/white_bird.png'), 3, 1, 50, 50, obstacle_group)

wolf = AnimatedSprite(load_image('graphics/damage/wolf.png'), 5, 1, 50, 50, obstacle_group)

pig = AnimatedSprite(load_image('graphics/damage/pig.png'), 3, 1, 50, 50, obstacle_group)

horse = AnimatedSprite(load_image('graphics/damage/horse.png'), 3, 1, 50, 50, obstacle_group)

board = load_image('graphics/platformes/board.png')

grass = load_image('graphics/platformes/grass.png')

coin = AnimatedSprite(load_image('graphics/coins/coin.png'), 7, 1, 40, 40, obstacle_group)

file = open('levels/1.txt', mode='r')
lev = file.readlines()
level = []
for el in lev:
    res = ''
    for elem in el:
        if elem == '\n' or elem == '':
            pass
        else:
            res += elem
    level.append(res)






all_skins = ['player', 'player1', 'player2']




player_stand = fairy_jump.frames[fairy_jump.cur_frame]
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(600, 260))






game_name = test_font.render("forest's secrets", False, (65, 72, 51))
game_name_rect = game_name.get_rect(center=(600, 150))

game_message = test_font.render('Log in', False, (65, 72, 51))
game_message_rect = game_message.get_rect(center=(600, 380))

#button = pygame.draw.rect(screen, (111, 196, 169), (300,400, 400, 450), 4)

#button_stand = load_image('graphics/login.png')
#button_stand = pygame.transform.rotozoom(button_stand, 0, 2)
#button_stand_rect = player_stand.get_rect(center=(200, 430))
#screen.blit(button_stand, button_stand_rect)

# Timer
obstacle_timer = pygame.USEREVENT + 1
board_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

#pygame.time.set_timer(board_timer, 1500)


box_width, box_height = 204, 204
box_x, box_y = (1200 - box_width) // 2 + 2, (800 - box_height) // 2
heart_width, heart_height = 16, 16
heart_speed = 5

#clock = pygame.time.Clock()


player_und = pygame.sprite.Group()
attack1 = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
enemy_sprite = pygame.sprite.Group()
attack_bar_group = pygame.sprite.Group()
line_group = pygame.sprite.Group()

heat_sound = pygame.mixer.Sound('data1/snd_curtgunshot.ogg')
spider_song = pygame.mixer.Sound('data1/mus_spider.ogg')
text_sound = pygame.mixer.Sound('data1/text.mp3')

big_font = pygame.font.Font('data1/Minecraft Rus NEW.otf', 40)
small_font = pygame.font.Font('data1/Minecraft Rus NEW.otf', 20)


tetris = [[0] * 10 for i in range(3)]




first_attack = False
player_und_attacking = False
draw_big_text = True
draw_attack_bar = False
enemy_attack_time = True
before_len_attack = 0

enemy_text = small_font.render('', True, 'white')
big_text = big_font.render('', True, 'white')
damage_text = small_font.render('', True, 'white')
enemy_hp = small_font.render('', True, 'white')
box_width, box_height = 204, 204

width, height = 1200, 800
box_x, box_y = (800) // 2 + 2, (600) // 2
heart_width, heart_height = 16, 16
heart_speed = 5



