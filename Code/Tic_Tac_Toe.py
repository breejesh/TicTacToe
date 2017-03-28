__author__ = 'Breejesh Rathod'

import sys
import pygame
from pygame.locals import *


FPS = 30

WIDTH = 700
HEIGHT = 500

RESOLUTION = (WIDTH, HEIGHT)

screen = None
clock = None
font = None

keys = {'Up': 0, 'Down': 0, 'Left': 0, 'Right': 0}
mouse = {'X': 0, 'Y': 0, 'LClick': 0, 'MClick': 0, 'RClick': 0}
mouse_pressed = False

game_flag = False

bg_image = None
bg_rect = None

logo_image = None
logo_rect = None

mode_image = None
mode_rect = None

board_image = None
board_rect = None
boardX_image = None
boardO_image = None

x_image = None
x_rect = None

o_image = None
o_rect = None

resultX_image = None
resultX_rect = None

resultO_image = None
resultO_rect = None

resultN_image = None
resultN_rect = None

current_turn = None
turns = None
winner = None

board = None
board_moves_rect = None

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def init_game():
    global game_flag, screen, font, clock, current_turn, turns, winner, board, board_moves_rect

    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption('Tic Tac Toe')
    pygame.mouse.set_visible(True)
    clock = pygame.time.Clock()


    current_turn = 'X'
    turns = 0
    winner = 0

    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    board_moves_rect = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    load_sprites()

    init_board_moves_rect()

    game_flag = True


def load_sprites():
    global bg_image, bg_rect, logo_image, logo_rect, mode_image, mode_rect, board_image, \
        board_rect, boardX_image, boardO_image, x_image, x_rect, o_image, o_rect, resultO_image,\
        resultO_rect, resultX_image, resultX_rect, resultN_image, resultN_rect

    bg_image = pygame.image.load('Sprites/bg.jpg')
    bg_rect = bg_image.get_rect()

    logo_image = pygame.image.load('Sprites/logo.png')
    logo_rect = logo_image.get_rect()

    mode_image = pygame.image.load('Sprites/mode.png')
    mode_rect = logo_image.get_rect()

    boardX_image = pygame.image.load('Sprites/boardX.png')
    boardO_image = pygame.image.load('Sprites/boardO.png')

    board_image = boardX_image
    board_rect = board_image.get_rect()

    x_image = pygame.image.load('Sprites/x.png')
    x_rect = x_image.get_rect()

    o_image = pygame.image.load('Sprites/o.png')
    o_rect = o_image.get_rect()

    resultX_image = pygame.image.load('Sprites/resultX.png')
    resultX_rect = resultX_image.get_rect()

    resultO_image = pygame.image.load('Sprites/resultO.png')
    resultO_rect = resultO_image.get_rect()
    
    resultN_image = pygame.image.load('Sprites/resultN.png')
    resultN_rect = resultN_image.get_rect()


def init_board_moves_rect():
    global board_moves_rect

    board_moves_rect[0] = (242, 172)
    board_moves_rect[1] = (320, 172)
    board_moves_rect[2] = (395, 172)

    board_moves_rect[3] = (242, 243)
    board_moves_rect[4] = (320, 243)
    board_moves_rect[5] = (395, 243)

    board_moves_rect[6] = (242, 321)
    board_moves_rect[7] = (320, 321)
    board_moves_rect[8] = (395, 321)
    pass


def check_mouse():
    global mouse, mouse_pressed

    mouse_pressed = False
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()

        if event.type == MOUSEBUTTONDOWN:
            mouse_pressed = True
            mouse['X'], mouse['Y'] = pygame.mouse.get_pos()
            mouse['LClick'], mouse['MClick'], mouse['RClick'] = pygame.mouse.get_pressed()
        else:
            mouse['X'], mouse['Y'] = 0, 0
            mouse['LClick'], mouse['MClick'], mouse['RClick'] = 0, 0, 0


def check_keyboard():
    global keys, key_pressed

    key_pressed = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()

        if event.type == KEYUP:
            if event.key == K_UP:
                keys['Up'] = 0
            elif event.key == K_DOWN:
                keys['Down'] = 0
            elif event.key == K_LEFT:
                keys['Left'] = 0
            elif event.key == K_RIGHT:
                keys['Right'] = 0
            elif event.key == K_RETURN:
                keys['Enter'] = 0

        if event.type == KEYDOWN:
            key_pressed = 1
            if event.key == K_UP:
                keys['Up'] = 1
            elif event.key == K_DOWN:
                keys['Down'] = 1
            elif event.key == K_LEFT:
                keys['Left'] = 1
            elif event.key == K_RIGHT:
                keys['Right'] = 1
            elif event.key == K_RETURN:
                keys['Enter'] = 1
            elif event.key == K_ESCAPE:
                terminate()
                key_pressed = 0


def clear_screen():
    screen.blit(bg_image, bg_rect)


def display_menu():
    screen.blit(logo_image, logo_rect)
    screen.blit(mode_image, mode_rect)


def display_sprites():
    if winner == 0:
        screen.blit(board_image, board_rect)
    for i in range(0, 9):
        if board[i] == 'X':
            x_rect.topleft = board_moves_rect[i]
            screen.blit(x_image, x_rect)
        elif board[i] == 'O':
            o_rect.topleft = board_moves_rect[i]
            screen.blit(o_image, o_rect)


def valid_move():

    if 242 < mouse['X'] < 300 and 172 < mouse['Y'] < 230:
        if board[0] == 0:
            board[0] = current_turn
            return True
    elif 320 < mouse['X'] < 370 and 172 < mouse['Y'] < 230:
        if board[1] == 0:
            board[1] = current_turn
            return True
    elif 395 < mouse['X'] < 450 and 172 < mouse['Y'] < 230:
        if board[2] == 0:
            board[2] = current_turn
            return True

    elif 242 < mouse['X'] < 300 and 243 < mouse['Y'] < 310:
        if board[3] == 0:
            board[3] = current_turn
            return True
    elif 320 < mouse['X'] < 370 and 243 < mouse['Y'] < 310:
        if board[4] == 0:
            board[4] = current_turn
            return True
    elif 395 < mouse['X'] < 450 and 243 < mouse['Y'] < 310:
        if board[5] == 0:
            board[5] = current_turn
            return True

    elif 242 < mouse['X'] < 300 and 321 < mouse['Y'] < 390:
        if board[6] == 0:
            board[6] = current_turn
            return True
    elif 320 < mouse['X'] < 370 and 321 < mouse['Y'] < 390:
        if board[7] == 0:
            board[7] = current_turn
            return True
    elif 395 < mouse['X'] < 450 and 321 < mouse['Y'] < 390:
        if board[8] == 0:
            board[8] = current_turn
            return True

    return False


def check_turn():
    global current_turn, board_image, turns

    if mouse_pressed:
        if valid_move():
            if current_turn == 'O':
                current_turn = 'X'
                board_image = boardX_image
            else:
                current_turn = 'O'
                board_image = boardO_image
            turns += 1


def check_result():
    global winner

    if turns > 4:
        if board[0] == board[1] == board[2] != 0 or board[0] == board[3] == board[6] != 0 or \
               board[0] == board[4] == board[8] != 0 or board[2] == board[5] == board[8] != 0 or \
                   board[6] == board[7] == board[8] != 0 or board[1] == board[4] == board[7] != 0 or \
                       board[3] == board[4] == board[5] != 0 or board[2] == board[4] == board[6] != 0:

            if current_turn == 'X':
                winner = 'O'
            else:
                winner = 'X'
            return True
        elif turns == 9:
            winner = 'N'
            return True
    return False


def display_result():
    clear_screen()
    display_sprites()
    if winner == 'X':
        screen.blit(resultX_image, resultX_rect)
    elif winner == 'O':
        screen.blit(resultO_image, resultO_rect)
    else:
        screen.blit(resultN_image, resultN_rect)
    pygame.display.update()


def play_again():
    while True:
        check_mouse()
        if mouse_pressed:
            if 552 < mouse['X'] < 613 and 270 < mouse['Y'] < 290:
                return True
            elif 565 < mouse['X'] < 606 and 295 < mouse['Y'] < 310:
                return False


def terminate():
    pygame.quit()
    sys.exit()


while True:
    init_game()
    clear_screen()
    display_menu()
    pygame.display.update()

    while True:
        check_mouse()
        if mouse_pressed:
            if 291 > mouse['X'] > 168 and 373 < mouse['Y'] < 417:
                break
    game_flag = True

    while game_flag:
        check_mouse()
        check_turn()
        clear_screen()
        display_sprites()
        pygame.display.update()
        if check_result():
            display_result()
            if play_again():
                init_game()
            else:
                game_flag = False
        clock.tick(FPS)
