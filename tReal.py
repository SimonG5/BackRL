from locale import windows_locale
from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

def build_agent(model,actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=50000,window_length = 1)
    dqn = DQNAgent(model=model,memory=memory,policy=policy)