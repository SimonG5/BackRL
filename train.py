from random import random
from env import Backgammon
from random import randint
import random
import tensorflow as tf
import numpy as np

RED = 1
BLACK = 0

model = tf.keras.models.load_model('model/policy.model')
env = Backgammon()

agent = randint(BLACK, RED)
env.reset()
done = False
score = 0
roll = []

while not done:
    if len(roll) == 0:
        roll = [randint(1, 6),randint(1, 6)]
        if roll[0] == roll[1]:
            roll.append(roll[0])
            roll.append(roll[0])
        if agent == RED:
            agent = BLACK
        else:
            agent = RED
            
    board = []
    board.extend(env.state.points)
    board.extend(env.state.barCheckers)
    board.extend(env.state.homeCheckers)
    board.append(roll[0])
    board.append(roll[1])
    board.append(agent)
    print(len(board))

    input = tf.keras.utils.normalize(board)
    predictions = model.predict([input])

    topThree = np.argsort(predictions[0])[-3:]
    action = None
    while True:
        action = random.choice(topThree)
        if env.state.isValidMove(agent,action):
            break
        else:
            action = random.choice(topThree)


    n_state, reward, done, info = env.step(agent,action)
    score += reward
print(score)

