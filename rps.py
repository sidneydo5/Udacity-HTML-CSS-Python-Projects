#!/usr/bin/env python3

import random
from colorama import init, Fore, Back, Style
init(autoreset=True)

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    moves = ['rock', 'paper', 'scissors']

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass
#       self.my_move = my_move
#       self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RockPlayer(Player):
    def move(self):
        return moves[0]


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move_person = input("What will it be: Rock, Paper or Scissors? > ")
            if move_person.lower() in self.moves:
                return move_person.lower()
            elif move_person.lower() == 'exit':
                exit()


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = self.moves

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        if self.my_move == self.moves[1]:
            return self.moves[2]
        elif self.my_move == self.moves[2]:
            return self.moves[0]
        else:
            return self.moves[1]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_Player1 = 0
        self.score_Player2 = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if self.beats(move1, move2):
            self.score_Player1 += 1
            print(Fore.GREEN + "Player 1 Wins!")
        elif move1 == move2:
            self.score_Player1 == self.score_Player1
            self.score_Player2 == self.score_Player2
            print(Fore.YELLOW + "Tie!")
        else:
            self.score_Player2 += 1
            print(Fore.RED + "Player 2 Wins!")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Player 1 Score: {self.score_Player1}"
              f"  Player 2 Score: {self.score_Player2}")

    def play_game(self):
        print("Rock, Paper, Scissors: Game start!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        print(f"Game over!\nFinal Score -- Player 1: "
              f"{self.score_Player1} Player 2: {self.score_Player2}")
        if self.score_Player1 == self.score_Player2:
            print(Fore.YELLOW + "The Game is a Tie.")
        elif self.score_Player1 > self.score_Player2:
            print(Fore.GREEN + "The User Wins!!!")
        else:
            print(Fore.RED + "The Computer Wins...")


if __name__ == '__main__':
    # game = Game(HumanPlayer(), random.choice([RandomPlayer(),
    #        ReflectPlayer(), CyclePlayer(), RockPlayer()]))
    players = [
        RockPlayer(),
        RandomPlayer(),
        ReflectPlayer(),
        CyclePlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(players)
    game = Game(p1, p2)
    game.play_game()
