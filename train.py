from env import Backgammon

env = Backgammon()

env.reset()
done = False
score = 0

while not done:
    action = env.action_space.sample()
    n_state, reward, done, info = env.step(action)
    score += reward
print(score)
