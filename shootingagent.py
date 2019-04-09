"""
file: shootingagent.py
language: python2.7
author 1: np9603@cs.rit.edu Nihal Surendra Parchand
author 2: rk4447@cs.rit.edu Rohit Girijan Kunjilikattil
"""


import argparse
import sys
import gym
import random
from gym import wrappers, logger
from PIL import Image

frame_skip = 0
shootcounter = -1
shoot_actions = [10, 14, 11, 16, 13, 17, 12, 15]


class Agent(object):
    """The world's simplest agent!"""

    def __init__(self, action_space):
        self.action_space = action_space

    # You should modify this function
    def act(self, observation, reward, done):
        global shootcounter    #  this variable is used maintain a counter to help select a serialized action in every move
        global frame_skip      #  this is used to skip the inital frames that are not necessary
        frame_skip +=1
        while frame_skip < 50:
            return 0

        enemy_present = False
        # The following code is used to identify whether an enemy is present or not
        for w in observation:
            for x, y, z in w:
                if not ((x == 84 and y == 92 and z == 214) or (x == 232 and y == 232 and z == 74) or (
                        x == 240 and y == 170 and z == 103) or (x == 0 and y == 0 and z == 0)):
                    enemy_present = True
                    break
                else:
                    continue
        # if enemy is present, the agent shoots, selecting a action from an array of action such that the actions are serialized
        if enemy_present == True:
            shootcounter += 1
            return shoot_actions[shootcounter % len(shoot_actions)]
        else:
            row = 0
            agentcoordinates = []
            wallcoordinates = []
            for w in observation:
                column = 0
                # The following code is used to create a list of lists of agent coordinates for each frame
                for x, y, z in w:
                    if (x == 240 and y == 170 and z == 103):
                        agentcoordinates.append([row, column])
                    elif (x == 84 and y == 92 and z == 214):
                        wallcoordinates.append([row, column])
                    column += 1
                row += 1

            distance = 0
            exit_distance = 0
            # This code is used to calculate the distance of the agent from the top wall and the exit in order to navigate to the exit
            for wcord in wallcoordinates:
                for acord in agentcoordinates:
                    distance = abs(acord[0] - wcord[0])
                    exit_distance = abs(acord[1] - wcord[1])
                    if distance < 10 and exit_distance < 65:
                        return 3
                    else:
                        return 2

        return 1


## YOU MAY NOT MODIFY ANYTHING BELOW THIS LINE OR USE
## ANOTHER MAIN PROGRAM
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument('--env_id', nargs='?', default='Berzerk-v0', help='Select the environment to run')
    args = parser.parse_args()
    # You can set the level to logger.DEBUG or logger.WARN if you
    # want to change the amount of output.
    logger.set_level(logger.INFO)
    env = gym.make(args.env_id)
    # You provide the directory to write to (can be an existing
    # directory, including one with existing data -- all monitor files
    # will be namespaced). You can also dump to a tempdir if you'd
    # like: tempfile.mkdtemp().
    outdir = 'random-agent-results'
    env.seed()
    agent = Agent(env.action_space)
    episode_count = 100
    reward = 0
    done = False
    score = 0
    special_data = {}
    special_data['ale.lives'] = 3
    ob = env.reset()
    action = agent.act(ob, reward, done)
    ob, reward, done, x = env.step(action)
    while not done:
        action = agent.act(ob, reward, done)
        ob, reward, done, x = env.step(action)
        score += reward
        env.render()
    # Close the env and write monitor result info to disk
    print("Your score: %d" % score)
    # For saving score
    # with open('shootingagentscore.txt', "a") as f:
    #     f.write(str(score) + '\n')
    env.close()