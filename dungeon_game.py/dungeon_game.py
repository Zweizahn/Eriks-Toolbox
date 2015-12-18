__author__ = 'Erik'

import random
import sys

CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]


def get_locations():
    while True:
        monster = random.choice(CELLS)
        door = random.choice(CELLS)
        start = random.choice(CELLS)
        if monster != door and monster != start and door != start:
            break

    return monster, door, start


def move_player(player, move):
    x, y = player
    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP':
        x -= 1
    elif move == 'DOWN':
        x += 1
    else:
        print('Illegal move {}, ending program'.format(move))
        sys.exit()
    return x, y


def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    x, y = player
    if y == 0:
        moves.remove('LEFT')
    if x == 0:
        moves.remove('UP')
    if y == 2:
        moves.remove('RIGHT')
    if x == 2:
        moves.remove('DOWN')

    return moves


################### Start main #####################
monster, door, start = get_locations()
player = start[:]

while True:
    print("Welcome to the dungeon!")
    print("You're currently in room {}".format(player))
    legal_moves = get_moves(player)
    print("You can move {}".format(legal_moves))
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break

    if move in legal_moves:
        player = move_player(player, move)
        if player == door:
            print('You win! Position of door is {}'.format(door))
            break
        elif player == monster:
            print('You lose! Position of monster is {}'.format(monster))
            break
    else:
        print('Illegal move, try again')
