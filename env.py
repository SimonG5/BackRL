from operator import truediv
from random import randint
from turtle import color, st
from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
from board import Board

RED = 1
BLACK = 0


class Backgammon(Env):
    def __init__(self):
        self.state = None
        self.current_agent = None
        self.action_space = Discrete(601)
        self.roll = []

    def step(self, action):
        if len(self.roll) == 0:
            self.roll()

        if self.state.isValidMove(self.state.outputMapping[action]):
            self.state.addCheckerToPoint(
                self.current_agent, self.state.outputMapping[action])

        reward = 0
        done = False

        if self.state.isGameOver() == 1:
            reward = 1
            done = True
        elif self.state.isGameOver() == -1:
            reward = -1
            done = True

        info = {}

        self.render()
        return self.state, reward, done, info

    def render(self):
        self.state.printBoard()

    def reset(self):
        roll = randint(1, 6), randint(1, 6)

        # roll the dice until they are different
        while roll[0] == roll[1]:
            roll = randint(1, 6), randint(1, 6)

        # set the current agent
        if roll[0] > roll[1]:
            self.current_agent = RED
        else:
            self.current_agent = BLACK

        self.roll = roll
        self.state = Board()

    def rollDice(self):
        roll = [randint(1, 6), randint(1, 6)]

        if roll[0] == roll[1]:
            roll.append(roll[0])
            roll.append(roll[0])

        if self.current_agent == BLACK:
            self.current_agent = RED
        else:
            self.current_agent = BLACK

        self.roll = roll
