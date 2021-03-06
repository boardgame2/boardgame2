import numpy as np
import pytest
import gym

import boardgame2


def test_reversi():
    env = gym.make('Reversi-v0')
    assert env.observation_space[0].shape == (8, 8)
    assert env.observation_space[1].shape == ()
    assert env.action_space.shape == (2,)
    assert np.all(env.action_space.high == [7, 7])
    
    observation = env.reset()
    while True:
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            break
    env.close()
