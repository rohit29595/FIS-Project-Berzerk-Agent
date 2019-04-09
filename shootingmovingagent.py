"""
file: shootingmovingagent.py
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


frame_skip=0   #Used to skip the initial frames which are of no use
shoot_actions = [10,14,11,16,13,17,12,15] # The list of shooting actions that the agent csn perform


class Agent(object):
    """The world's simplest agent!"""

    def __init__(self, action_space):
        self.action_space = action_space
        self.action_index = 0

    # You should modify this function

    def act(self, observation, reward, done):
        global frame_skip
        frame_skip +=1
        while frame_skip < 50:
            return 0
        enemy_present = False

     # The following code is used to scan every pixel from the observation to identify whether an enemy is present or not

        for w in observation:
            for x, y, z in w:
                if not ((x == 84 and y == 92 and z == 214) or (x == 232 and y == 232 and z == 74) or (
                        x == 240 and y == 170 and z == 103) or (x == 0 and y == 0 and z == 0)):

                    enemy_present = True
                    break
                else:
                    continue
            if enemy_present == True:
                break
            else:
                continue

        if enemy_present == True:
            return random.randint(10,17)
        else:

            row = 0
            agentcoordinates = []
            wallcoordinates = []

        # This following code is used in oder to decide which move to take up next
            for w in observation:
                column = 0
                for x, y, z in w:
                    if (x == 240 and y == 170 and z == 103):
                        agentcoordinates.append([row, column])
                    elif (x == 84 and y == 92 and z == 214):
                        wallcoordinates.append([row, column])
                    column += 1
                row += 1


            distance=0
            exit_distance=0

        # This code checks the distance of the agent with the top wall and the exit to navigate to the exit
            for wcord in wallcoordinates:
                for acord in agentcoordinates:
                    distance = abs(acord[0]-wcord[0])
                    exit_distance = abs(acord[1]-wcord[1])
                    if distance<10:
                        if exit_distance>=65 and exit_distance<=100:
                            return 2
                        elif exit_distance<65:
                            return 3
                        elif exit_distance>100:
                            return 4
                    else:
                        action=2
                    return action
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
        # with open('shootingmovingagentscore.txt', "a") as f:
        #     f.write(str(score) + '\n')
        env.close()
