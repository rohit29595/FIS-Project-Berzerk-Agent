"""
file: anova.py
language: python2.7
author 1: np9603@cs.rit.edu Nihal Surendra Parchand
author 2: rk4447@cs.rit.edu Rohit Girijan Kunjilikattil
"""

import scipy.stats as sc
import pandas as pd
import matplotlib.pyplot as plt

# Read and save scores of each agent into a dataframe
dataset1=pd.read_csv('randomagentscore.txt',sep='\n', header=None)
dataset2=pd.read_csv('shootingagentscore.txt',sep='\n', header=None)
dataset3=pd.read_csv('shootingmovingagentscore.txt',sep='\n', header=None)

# Perform one-way Anova test
anova_results=sc.stats.f_oneway(dataset1,dataset2,dataset3)
print(anova_results)

dataset1['agent1']=(dataset2).astype(int)
dataset1['agent2']=(dataset3).astype(int)
dataset1.columns = ['random','shooting agent','shooting moving agent']

# Plot Histogram for the scores
hist = dataset1.plot.hist(bins=15,histtype='barstacked')
plt.title('Statistical Analysis-Histogram')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.grid()
plt.savefig('histogram.png')
plt.show()