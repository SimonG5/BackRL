from gym import Env
from gym.spaces import Discrete
from board import Board

RED = 1
BLACK = 0


class Backgammon(Env):
    def __init__(self):
        self.state = None
        self.current_agent = None
        self.action_space = Discrete(601)

    def step(self,agent, action):
        if self.state.isValidMove(self.state.outputMapping[action]):
            self.state.addCheckerToPoint(agent, self.state.outputMapping[action])

        reward = 0
        done = False

        if self.state.isGameOver() == 1:
            reward = 1
            done = True
        elif self.state.isGameOver() == -1:
            reward = -1
            done = True

        info = {}

        return self.state, reward, done, info

    def render(self):
        self.state.printBoard()

    def reset(self):
        self.state = Board()

