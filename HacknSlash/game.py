__author__ = 'Erik'

from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll
import sys


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        if self.monster.attack():
            print("Monster {} is attacking".format(self.monster))
            if not self.player.dodge():
                self.player.hit_points -= 1
        else:
            print("Monster {} does not attack".format(self.monster))

            # check to see if the monster attacks
            # if so, tell the player
            # check if the player wants to dodge
            # if so, see if the dodge is successful
            # if it is, move on
            # if it's not, remove one player hit point

    # if the monster isn't attacking, tell that too

    def player_turn(self):
        choice = input("[A]ttack, [R]est or [Q]uit?").lower()
        if choice == 'a':
            if self.player.attack():
                if self.monster.dodge():
                    print("Monster {} dodges".format(self.monster))
                else:
                    print("Monster {} doesn't dodge".format(self.monster))
                    if self.player.leveled_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1
        elif choice == 'r':
            self.player.rest()
        elif choice == 'q':
            print(self.monster)
            print(self.player)
            print("Exit game")
            sys.exit()
        else:
            self.player_turn()

            # let the player attack, rest, or quit
            # if they attack:
            # see if the attack is successful
            # if so, see if the monster dodges
            # if dodged, print that
            # if not dodged, subtract the right num hit points from the monster
            # if not a good attack, tell the player
            # if they rest:
            # call the player.rest() method

    # if they quit, exit the game
    # if they pick anything else, re-run this method

    def cleanup(self):
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experience
            print("Level up player")
            self.monster = self.get_next_monster()

            # if the monster has no more hit points:
            # up the player's experience
            # print a message
            # get a new monster

    def __init__(self):
        self.setup()

        while self.player.hit_points and (self.monster or self.monsters):
            print(self.player)
            print(self.monster)
            self.monster_turn()
            self.player_turn()
            self.cleanup()
            print("\n")

        if self.player.hit_points:
            print("You win!")
        elif self.monsters or self.monster:
            print("You lose!")

        sys.exit()


Game()