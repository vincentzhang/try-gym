import gym

#ENV = 'MountainCar-v0'
#ENV = 'CartPole-v0'
#ENV = 'MsPacman-v0'
#ENV = 'Hopper-v2'
#env = gym.make(ENV)
from gym.envs import mujoco, robotics
#env = mujoco.AntEnv()
#env = mujoco.HumanoidEnv()
#env = robotics.FetchReachEnv()
env = robotics.FetchPickAndPlaceEnv()
#env = robotics.HandReachEnv()

env.reset()

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())

env.close()
