# MINE RL INTRO

# SOME TIMES IT WILL WORK OTHER TIMES IT WONT BE NICE MAYBE IT WILL LIKE YOU

import minerl
import gym
import logging
logging.basicConfig(level=logging.DEBUG)

# minerl.data.download("/MineRLData", experiment='MineRLNavigateDense-v0')
env = gym.make('MineRLNavigateDense-v0')


obs = env.reset()
done = False
net_reward = 0

while not done:
    action = env.action_space.noop()

    action['camera'] = [0, 0.03*obs["compassAngle"]]
    action['back'] = 0
    action['forward'] = 1
    action['jump'] = 1
    action['attack'] = 1

    obs, reward, done, info = env.step(
        action)

    net_reward += reward
    print("Total reward: ", net_reward)

