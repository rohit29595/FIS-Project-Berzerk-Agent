"""
file: boxplot.py
language: python2.7
author 1: np9603@cs.rit.edu Nihal Surendra Parchand
author 2: rk4447@cs.rit.edu Rohit Girijan Kunjilikattil
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read and save scores of each agent into a dataframe
dataset1=pd.read_csv('randomagentscore.txt',sep='\n', header=None)
dataset2=pd.read_csv('shootingagentscore.txt',sep='\n', header=None)
dataset3=pd.read_csv('shootingmovingagentscore.txt',sep='\n', header=None)

dataset1['shooting agent']=(dataset2).astype(int)
dataset1['shooting moving agent']=(dataset3).astype(int)
dataset1.columns = ['random','shooting agent','shooting moving agent']
print(dataset1)

# Plot boxplot for the scores
boxplot = dataset1.boxplot()
plt.title('Comparison of agents')
plt.xlabel('Agents')
plt.ylabel('Scores')
plt.savefig('boxplot.png')
plt.show()

