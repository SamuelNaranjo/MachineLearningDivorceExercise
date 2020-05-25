#A01205900 FINAL PROJECT
#LOGISTIC REGRESSION ALGORITHM APPLIED IN A DIVORCE CHANCE PROBLEM
#
#
#
import random
from random import seed
from random import randrange
from math import exp
#import matplotlib.pyplot as plt

#VALUES USED FOR ALGORITHM
nfolds = 3
lrnrate =.001
numepoch = 500
#Dataset
dataset = [[2,2,4,1,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,2,1,2,0,1,2,1,3,3,2,1,1,2,3,2,1,3,3,3,2,3,2,1,1],
           [4,4,4,4,4,0,0,4,4,4,4,3,4,0,4,4,4,4,3,2,1,1,0,2,2,1,2,0,1,1,0,4,2,3,0,2,3,4,2,4,2,2,3,4,2,2,2,3,4,4,4,4,2,2,1],
           [2,2,2,2,1,3,2,1,1,2,3,4,2,3,3,3,3,3,3,2,1,0,1,2,2,2,2,2,3,2,3,3,1,1,1,1,2,1,3,3,3,3,2,3,2,3,2,3,1,1,1,2,2,2,1],
           [3,2,3,2,3,3,3,3,3,3,4,3,3,4,3,3,3,3,3,4,1,1,1,1,2,1,1,1,1,3,2,3,2,2,1,1,3,3,4,4,2,2,3,2,3,2,2,3,3,3,3,2,2,2,1],
           [2,2,1,1,1,1,0,0,0,0,0,1,0,1,1,1,1,1,2,1,1,0,0,0,0,2,1,2,1,1,1,1,1,1,0,0,0,0,2,1,0,2,3,0,2,2,1,2,3,2,2,2,1,0,1],
           [0,0,1,0,0,2,0,0,0,1,0,2,1,0,2,0,2,1,0,1,0,0,0,0,2,2,0,0,0,0,4,1,1,1,1,1,1,2,0,2,2,1,2,3,0,2,2,1,2,1,1,1,2,0,1],
           [3,3,3,2,1,3,4,3,2,2,2,2,2,3,2,3,3,3,3,2,3,3,3,3,2,3,3,2,2,2,1,2,2,1,1,2,3,2,2,3,3,3,3,4,3,3,2,3,2,3,3,2,2,2,1],
           [2,1,2,2,2,1,0,3,3,2,4,3,2,3,4,3,2,3,2,1,2,1,1,2,3,3,2,2,2,3,1,1,0,2,2,1,4,4,4,4,4,4,3,2,0,0,1,2,2,2,1,1,1,0,1],
           [2,2,1,0,0,4,1,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,3,2,3,2,3,2,3,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,2,0,2,2,2,3,0,0,2,1,0,1,2,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,2,2,1,2,3,2,2,2,0,2,2,2,2,4,3,3,1],
           [4,4,4,3,4,0,0,4,4,3,4,4,4,4,4,3,4,4,4,4,4,3,4,4,4,4,4,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [4,4,4,3,4,0,0,4,4,3,4,4,4,4,4,3,4,4,4,4,4,3,4,4,4,4,4,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,4,3,4,3,0,1,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,4,3,4,3,0,1,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,4,3,4,3,0,1,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,4,4,4,4,4,4,4,4,4,4,1],
           [4,4,3,2,4,0,0,4,3,2,4,4,4,4,3,2,4,4,4,4,3,2,4,4,4,4,3,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [4,4,3,2,4,0,0,4,3,2,4,4,4,4,3,2,4,4,4,4,3,2,4,4,4,4,3,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [4,4,4,3,4,0,0,4,4,3,4,4,4,4,4,3,4,4,4,4,4,3,4,4,4,4,4,3,4,4,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,4,3,4,3,4,1],
           [3,3,4,4,3,1,1,3,4,4,3,3,3,3,4,4,3,3,3,3,4,4,3,3,3,3,4,4,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [4,4,4,3,4,0,0,4,4,3,4,4,4,4,4,3,4,4,4,4,4,3,4,4,4,4,4,3,4,4,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,4,3,4,3,4,1],
           [4,3,3,3,4,1,0,3,3,3,4,3,4,3,3,3,4,3,4,3,3,3,4,3,4,3,3,3,4,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [4,3,3,3,4,1,0,3,3,3,4,3,4,3,3,3,4,3,4,3,3,3,4,3,4,3,3,3,4,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,4,4,4,3,0,1,4,4,4,3,4,3,4,4,4,3,4,3,4,4,4,3,4,3,4,4,4,3,4,4,3,4,3,4,3,4,3,4,3,4,3,4,3,3,3,4,3,4,4,3,4,3,4,1],
           [3,3,3,4,3,1,1,3,3,4,3,3,3,3,3,4,3,3,3,3,3,4,3,3,3,3,3,4,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [4,2,3,4,4,2,0,2,3,4,4,2,4,2,3,4,4,2,4,2,3,4,4,2,4,2,3,4,4,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,3,3,4,3,1,1,3,3,4,3,3,3,3,3,4,3,3,3,3,3,4,3,3,3,3,3,4,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,3,4,3,3,1,1,3,4,3,3,3,3,3,4,3,3,3,3,3,4,3,3,3,3,3,4,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,4,4,4,4,4,4,4,4,4,1],
           [3,3,3,4,3,1,1,3,3,4,3,3,3,3,3,4,3,3,3,3,3,4,3,3,3,3,3,4,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,4,4,4,4,4,4,4,4,4,1],
           [3,4,3,2,3,0,1,4,3,2,3,4,3,4,3,2,3,4,3,4,3,2,3,4,3,4,3,2,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [4,3,3,2,4,1,0,3,3,2,4,3,4,3,3,2,4,3,4,3,3,2,4,3,4,3,3,2,4,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,4,3,2,3,0,1,4,3,2,3,4,3,4,3,2,3,4,3,4,3,2,3,4,3,4,3,2,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [4,3,4,3,4,1,0,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,4,3,4,3,4,1],
           [4,3,3,4,4,1,0,3,3,4,4,3,4,3,3,4,4,3,4,3,3,4,4,3,4,3,3,4,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,4,3,4,3,4,1],
           [3,4,2,3,3,0,1,4,2,3,3,4,3,4,2,3,3,4,3,4,2,3,3,4,3,4,2,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,4,4,4,4,4,4,4,4,4,1],
           [3,4,4,3,3,0,1,4,4,3,3,4,3,4,4,3,3,4,3,4,4,3,3,4,3,4,4,3,3,4,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,4,3,4,3,4,1],
           [3,3,3,3,3,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [4,3,3,3,4,1,0,3,3,3,4,3,4,3,3,3,4,3,4,3,3,3,4,3,4,3,3,3,4,3,4,3,4,3,4,3,4,4,3,4,4,4,4,3,4,4,3,4,4,3,3,4,4,3,1],
           [4,3,3,3,4,1,0,3,3,3,4,3,4,3,3,3,4,3,4,3,3,3,4,3,4,3,3,3,4,3,4,3,4,3,4,3,4,4,3,4,4,4,4,3,4,4,3,4,4,3,3,4,4,3,1],
           [3,3,2,3,3,1,1,3,3,3,4,3,3,3,3,3,3,3,4,3,3,3,3,4,3,3,2,4,3,4,4,4,4,4,4,4,4,4,4,4,4,3,4,3,3,3,4,4,4,4,3,3,4,4,1],
           [3,3,2,3,3,1,1,3,3,3,4,3,3,3,3,3,3,3,4,3,3,3,3,4,3,3,2,4,3,4,4,4,4,4,4,4,4,4,4,4,4,3,4,3,3,3,4,4,4,4,3,3,4,4,1],
           [4,3,3,3,4,1,0,3,3,3,4,3,4,3,3,3,4,3,4,3,3,3,4,3,4,3,3,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,4,3,4,3,4,1],
           [3,2,3,4,3,2,1,2,3,4,3,2,3,2,3,4,3,2,3,2,3,4,3,2,3,2,3,4,3,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,4,4,4,4,4,4,4,4,4,1],
           [4,2,3,2,4,2,0,2,3,2,4,2,4,2,3,2,4,2,4,2,3,2,4,2,4,2,3,2,4,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,4,3,3,3,0,1,4,3,3,3,4,3,4,3,3,3,4,3,4,3,3,3,4,3,4,3,3,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,3,4,3,4,3,1],
           [3,3,3,2,3,1,1,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [4,2,3,2,4,2,0,2,3,2,4,2,4,2,3,2,4,2,4,2,3,2,4,2,4,2,3,2,4,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,3,2,3,3,1,1,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,3,3,2,3,1,1,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,3,2,3,3,1,1,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [4,2,3,2,4,2,0,2,3,2,4,2,4,2,3,2,4,2,4,2,3,2,4,2,4,2,3,2,4,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,3,3,2,3,1,1,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [4,2,3,2,4,2,0,2,3,2,4,2,4,2,3,2,4,2,4,2,3,2,4,2,4,2,3,2,4,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,3,3,2,3,1,1,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,4,4,4,4,4,4,4,4,4,1],
           [4,3,2,3,4,1,0,3,2,3,4,3,4,3,2,3,4,3,4,3,2,3,4,3,4,3,2,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,4,3,4,3,4,1],
           [3,3,3,4,3,1,1,3,3,4,3,3,3,3,3,4,3,3,3,3,3,4,3,3,3,3,3,4,3,3,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,3,4,3,4,3,1],
           [4,3,3,2,4,1,0,3,3,2,4,3,4,3,3,2,4,3,4,3,3,2,4,3,4,3,3,2,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,3,3,4,3,4,4,3,4,3,4,1],
           [4,3,2,3,4,1,0,3,2,3,4,3,4,3,2,3,4,3,4,3,2,3,4,3,4,3,2,3,4,3,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,3,4,3,4,3,1],
           [3,4,3,4,3,0,1,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1],
           [3,4,3,4,3,0,1,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1],
           [3,3,3,3,3,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,4,3,4,3,4,1],
           [3,2,3,2,3,2,1,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,2,3,2,3,2,1,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,2,2,3,3,2,1,2,2,3,3,2,3,2,2,3,3,2,3,2,2,3,3,2,3,2,2,3,3,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,2,3,2,3,2,1,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,2,3,2,3,2,1,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,3,4,4,3,1,1,3,4,4,3,3,3,3,4,4,3,3,3,3,4,4,3,3,3,3,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1],
           [3,3,3,2,3,1,1,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,4,3,4,3,4,1],
           [3,3,2,3,3,1,1,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,4,3,4,3,4,1],
           [4,2,2,3,4,2,0,2,2,3,4,2,4,2,2,3,4,2,4,2,2,3,4,2,4,2,2,3,4,2,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,4,3,4,3,4,1],
           [3,3,3,2,3,1,1,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,3,3,4,3,4,4,3,4,3,4,1],
           [4,4,4,3,4,2,4,4,4,3,4,4,4,4,4,4,4,4,4,4,4,3,0,4,0,4,4,0,4,4,0,4,4,0,1,0,2,0,4,0,2,4,4,1,4,0,4,4,4,3,4,4,4,4,1],
           [3,3,3,2,3,1,1,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,3,4,3,4,3,1],
           [2,2,3,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,4,4,4,4,4,4,4,4,4,4,4,3,4,4,4,4,4,4,4,4,4,4,4,4,1],
           [3,3,3,3,3,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1],
           [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,2,1,1,1,0,0,2,0,1,0,1,0,0,0,0,0,0,2,2,2,2,1,0,0,0],
           [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,3,2,0,2,2,2,2,2,2,2,0],
           [0,3,1,0,0,0,0,0,0,0,0,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,4,0,0,2,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,4,2,0,0,0,0,0,0,0,0,1,4,2,0,4,2,1,1,0,0,0,1,0,0,0],
           [0,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,2,1,4,2,3,0,0,0,2,4,1,0],
           [0,1,2,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,2,2,0,1,0,1,2,0,0,0,3,2,1,0],
           [0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,0,1,0,0,1,0,0,0,0,0,2,0,2,2,1,2,0,0,0,4,4,0,0],
           [0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,0,2,0,1,0,0,0,0,0,0,0,0,3,0,0,2,2,0,0,1,1,3,4,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,4,2,3,1,1,2,0,0,1,4,1,2,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,2,0,3,0,3,3,1,2,1,1,1,0,1,0,0],
           [0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,3,4,3,0,2,2,2,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,2,2,2,0,0,2,2,2,2,1,1,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,4,0,4,3,1,3,1,3,3,3,1,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,4,0,0,0,0,0,0,0,0,3,0,2,2,2,2,4,4,0,0],
           [0,0,3,0,0,1,0,0,0,0,0,2,0,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,2,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,3,3,2,2,0,0,0,0],
           [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,1,0,0,1,0,0,0,1,1,2,0,1,2,2,2,2,2,2,2,2,2,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,3,2,1,3,0,2,3,3,2,1,0,0,0],
           [1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,3,3,3,3,1,1,0,0],
           [0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,2,3,1,3,3,3,2,1,1,1,1,1,1,0],
           [0,2,2,1,0,0,0,0,0,2,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,3,0,0,0,0,2,1,0,2,0,0,0,0,0,0,0,3,1,1,1,0,3,0,0],
           [0,1,1,0,0,0,0,0,0,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,1,0,1,0,3,1,4,0,2,2,0,1,0,0,1,0,0],
           [0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,2,0,1,4,4,3,3,1,2,3,1,1,0],
           [0,0,0,0,0,2,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,2,4,0,4,3,1,1,2,2,2,1,0,0,0],
           [0,0,0,0,0,1,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,2,1,2,2,3,3,2,0],
           [0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,4,1,1,4,4,2,2,0,1,0],
           [0,1,1,0,0,2,0,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,2,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,2,1,1,1,0,0],
           [0,0,0,0,0,2,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,1,0,0,4,2,0,1,2,1,3,1,1,1,1,1,0,0],
           [0,2,2,1,0,0,0,0,0,2,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,3,0,0,0,0,2,1,1,0,2,0,0,0,0,0,0,3,1,1,1,0,3,0,0],
           [0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,2,0,1,0,0,0,2,0,1,2,1,3,3,2,2,2,2,0,0],
           [0,0,0,0,0,2,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,2,1,0,3,0,2,3,4,3,3,0,2,0],
           [0,1,1,0,0,0,0,0,0,0,0,1,3,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,2,4,0,2,4,0,3,0,1,2,2,2,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,2,1,2,2,4,2,4,0,0,0,1,1,2,1,0,2,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,2,1,2,2,4,2,4,0,0,0,1,1,2,1,0,2,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,3,2,1,3,3,0,2,3,2,2,4,1,1,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,3,0,0,4,1,1,0,1,0,0,0,0,0,0,0,0,0,4,2,2,2,0],
           [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,4,4,0,4,1,4,2,3,2,2,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,0,1,2,2,2,2,2,2,2,2,0,1,0,0],
           [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,0,0,2,1,2,2,1,2,2,0,1,3,0,2,2,2,2,0,0,0,0],
           [0,0,2,0,2,4,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,3,0,1,0,0,1,0,0,0,1,0,4,0,1,1,2,3,0,1,1,0,0,0,0],
           [1,2,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,0,2,1,0,1,0,0,1,0,0,0,1,0,2,0,0,2,1,2,2,2,2,2,1,0,0],
           [1,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,1,0,0,0,0,2,0,2,0,2,3,0,3,3,3,2,2,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,0,0,0,1,1,0,0,3,2,1,2,2,1,2,3,2,2,3,1,1,0],
           [0,0,2,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,2,1,0,2,3,0,1,0,2,0,0,0,0,0,2,3,1,2,1,2,1,2,2,0,0],
           [0,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,2,2,0,3,3,3,3,0,1,3,3,3,1,0],
           [0,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,2,2,0,3,3,3,3,0,1,3,3,3,1,0],
           [3,1,1,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,1,1,1,0,3,3,2,2,0,2,2,0,0,4,0],
           [0,2,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,2,0,0,0,1,0,0,1,1,2,0,1,2,3,0,1,1,2,2,1,0,1,3,2,2,0],
           [0,1,2,0,0,0,0,0,0,1,1,1,2,1,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,2,1,1,1,1,1,1,0],
           [4,3,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,0,0,0,0],
           [3,0,0,0,0,0,0,0,0,0,0,1,1,2,1,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,3,2,4,4,0,1,0,0,1,4,1,0,0],
           [0,0,2,4,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,0,0,0,2,0,0,2,2,3,0,3,2,0,2,4,0,0,1,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,0,1,3,4,0,4,3,4,3,1,3,3,0,1,0,0],
           [2,1,1,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,1,1,0,0,0,0,1,0,2,0,0,1,0,2,1,2,1,3,1,3,1,1,3,0,0,0,0,0,0,0],
           [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,2,2,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,0,4,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,2,0,1,1,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,0,2,0,0,1,0,0,1,0,2,0,1,3,2,0,1,3,3,2,2,1,1,2,0,0,0],
           [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,4,4,4,4,4,4,4,2,2,0,0,0,0],
           [0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,4,4,0,4,4,4,3,1,1,1,2,0,1,0],
           [0,1,1,1,1,0,0,0,0,0,1,1,2,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,1,3,1,2,1,2,2,2,2,1,0],
           [1,0,0,0,0,1,0,0,0,1,1,0,1,1,1,1,0,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,2,4,1,0,2,1,2,1,2,2,4,2,0,0],
           [2,2,3,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,2,0,2,2,1,1,1,1,1,1,1,1,0],
           [1,0,1,0,1,1,0,0,0,1,0,0,1,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,0,0,2,1,2,2,2,2,3,0],
           [2,1,0,2,0,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,3,0,2,2,2,2,2,2,1,0],
           [0,0,1,1,0,0,0,0,0,2,1,2,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,2,1,0,2,0,0,1,1,1,1,0,2,2,0,0,2,1,2,1,2,2,1,0,0,0],
           [0,1,0,0,0,1,0,2,0,0,1,0,1,0,0,0,0,0,0,0,0,0,2,2,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,3,1,1,0,1,3,3,2,0,0,0,4,4,2,0],
           [0,1,0,1,0,0,0,0,0,1,1,2,2,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,2,1,0,0,0,0,1,1,2,1,0,2,2,2,1,0,1,3,2,2,2,1,0,0,0],
           [0,0,0,0,0,0,0,0,0,1,0,1,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,0,0,1,1,2,1,1,3,2,0,2,1,2,3,2,2,2,1,1,0,0],
           [2,0,2,0,0,0,0,0,0,2,0,0,2,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0,2,1,0,0,3,2,2,1,1,1,1,2,1,0],
           [1,1,2,0,2,1,0,2,1,2,1,1,2,0,2,1,2,1,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,2,2,0,1,1,0],
           [0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,2,2,4,4,4,2,2,2,2,4,2,2,0],
           [2,0,1,0,0,0,0,0,0,2,1,0,1,0,2,2,1,0,0,0,1,0,0,1,0,1,0,0,0,0,2,0,0,0,0,0,2,2,1,0,0,2,2,1,2,3,0,2,0,0,2,1,0,0,0],
           [2,1,1,0,0,2,0,0,0,2,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,2,2,0,0,0,0,0,0,1,0,1,2,0,1,0,3,1,1,3,1,1,1,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,3,4,0,0,4,0,1,0,1,0,0,0,0,1,0,4,1,1,4,2,2,2,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,3,1,3,4,1,2,2,2,2,3,2,2,0],
           [1,1,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,1,1,1,0,1,0,0,1,1,1,2,1,3,3,0,2,3,0,2,0,1,1,3,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,4,1,2,1,1,0,4,3,3,2,2,3,2,4,3,1,0],
           [0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,1,3,0,0,0,0,0,0,0,0,0,2,2,0,1,3,4,4,0,1,3,3,3,1,0],
           ]
#PREPARING THE DATA 
# SPLITING DATA IN K FOLDS (BOOK PAGE: 99)
def model_validation(dataset, nfolds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / nfolds)
	for _ in range(nfolds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

#ESTIMATING LOG REGRESSION COEFFICIENTS
def weightcalc(trainset, lrnrate, epoch):
	coef = [0.0 for i in range(len(trainset[0]))]
	for _ in range(numepoch):
		for realval in trainset:
			hyp = predict(realval, coef)
			error = realval[-1] - hyp
			coef[0] = coef[0] + lrnrate *error * hyp * (1.0 - hyp)
			for i in range(len(realval)-1):
				coef[i + 1] = coef[i + 1] +  lrnrate *error * hyp * (1.0 - hyp) * realval[i]
				
	return coef

#MODEL FITTING
def fitting_method(trainset, testset, lrnrate, epoch):
	predictions = list()
	coef = weightcalc(trainset, lrnrate, numepoch)
	for realval in testset:
		hyp = predict(realval, coef)
		hyp = round(hyp)
		predictions.append(hyp) 
	return(predictions)

#PREDICTING THE CLASS OF OUR DATA
def predict(realval, weights):
	hyp = weights[0]
	for i in range(len(realval)-1):
		hyp += weights[i + 1] * realval[i]
	return 1.0 / (1.0 + exp(-hyp))

#ACCURACY OF THE MODEL
def modelaccuracy(actual, ModelValue):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == ModelValue[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0 

#MODEL EVALUATION WITH THE NFOLDS
def model_evaluation(dataset, algorithm, nfolds, *args):
	folds = model_validation(dataset, nfolds)
	accpercentage = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		testset_set = list()
		for realval in fold:
			realval_copy = list(realval)
			testset_set.append(realval_copy)
			realval_copy[-1] = None
		ModelValue = algorithm(train_set, testset_set, *args)
		actual = [realval[-1] for realval in fold]
		accuracy = modelaccuracy(actual, ModelValue)
		accpercentage.append(accuracy)
	return accpercentage


seed(1)
accpercentage = model_evaluation(dataset, fitting_method, nfolds, lrnrate, numepoch)
#print('accpercentage: %s' % accpercentage)
print('Average Accuracy: %.3f%%' % (sum(accpercentage)/float(len(accpercentage))))
coef = weightcalc(dataset, lrnrate, numepoch)
print(coef)

#NEVER BEFORE SEEN DATA
notseendata = [[4,3,3,3,3,1,4,0,4,3,3,3,3,4,3,3,3,3,3,3,3,3,2,2,2,2,3,2,2,2,2,4,3,3,3,3,3,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1],
           [3,2,3,2,3,2,1,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,4,3,4,3,4,3,4,3,4,3,3,3,4,3,4,3,4,3,3,4,3,4,3,1],
           [4,4,3,3,4,0,4,2,4,4,3,4,4,4,4,4,4,4,4,4,0,0,2,4,4,4,4,1,1,0,4,2,0,0,0,0,3,0,4,4,4,4,4,4,4,2,4,4,3,4,4,1,1,0,1],
           [3,2,4,3,3,2,3,2,2,3,4,3,2,3,1,3,3,3,3,4,2,1,0,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,3,0,0,0,0,0,3,3,3,3,3,3,3,1],
           [2,2,2,3,2,3,2,1,3,2,1,2,2,2,3,3,3,3,3,2,2,1,1,3,3,3,2,3,2,2,3,3,3,3,3,3,3,3,4,4,4,4,3,4,2,2,3,3,2,1,1,2,2,2,1],
           [3,2,4,3,3,2,3,2,2,3,4,3,2,2,1,3,3,3,3,4,2,1,0,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,3,0,0,3,0,0,0,3,3,3,3,3,3,3,1],
           [4,2,4,2,1,2,3,1,1,3,3,3,2,2,3,2,2,3,3,2,2,2,2,3,4,4,3,3,3,4,4,4,2,2,0,0,4,3,4,4,3,1,1,4,1,2,1,3,3,3,3,1,1,1,1],
           [2,0,2,4,2,2,4,3,4,3,2,3,3,0,4,4,3,3,3,2,2,1,2,0,0,0,0,0,2,2,3,3,3,3,3,3,3,3,1,3,2,3,3,4,4,2,3,2,2,3,3,4,2,2,1],
           [4,4,3,3,2,0,2,4,4,3,4,3,4,3,4,4,4,3,3,3,2,3,3,3,3,3,1,3,3,2,3,3,3,4,4,4,4,4,4,4,4,2,2,3,2,2,2,2,2,3,3,3,3,4,1],
           [4,4,3,4,4,0,0,4,4,4,4,4,4,4,4,3,3,4,4,3,2,2,3,1,2,2,1,3,2,2,3,3,1,2,1,4,4,3,3,3,1,3,3,3,3,1,2,3,2,2,2,2,1,2,1],
           [3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,2,0,0,0,0,0,2,3,3,3,4,4,4,4,4,4,4,4,1,1,1,1,1,1,3,2,2,2,4,4,4,1],
           [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,3,1,0,0,1,1,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,2,0,1,1,1,1,0,0,0,1,1,1,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,3,0,0,0,0,2,0,0,1,2,2,1,0],
           [4,0,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0],
           [0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,0,3,0,1,0,0,0,2,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,2,0,0,2,0,2,3,2,2,1,1,0,0],
           [1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,2,0,2,1,0,0,1,1,1,1,1,1,0],
           [0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,2,1,0,0,0,2,1,1,1,1,2,1,1,1,0,0,0,0]]

random.shuffle(notseendata)

for realval in notseendata:
	hyp = predict(realval, coef)
	print("RealValue=%.3f, ModelValue=%.3f [%d]" % (realval[-1], hyp, round(hyp)))

#plt.plot(accpercentage)
#plt.show()


questionaire = ['1. If one of us apologizes when our discussion deteriorates, the discussion ends ',
'2. I know we can ignore our differences, even if things get hard sometimes ',
'3. When we need it, we can take our discussions with my spouse from the beginning and correct it ',
'4. When I discuss with my spouse, to contact him will eventually work ',
'5. The time I spent with my wife is special for us ',
'6. We dont have time at home as partners',
'7. We are like two strangers who share the same environment at home rather than family ',
'8. I enjoy our holidays with my wife',
'9. I enjoy traveling with my wife',
'10. Most of our goals are common to my spouse. ',
'11. I think that one day in the future, when I look back, I see that my spouse and I have been in harmony with each other. ',
'12. My spouse and I have similar values in terms of personal freedom. ',
'13. My spouse and I have similar sense of entertainment. ',
'14. Most of our goals for people children, friends, etc., are the same. ',
'15. Our dreams with my spouse are similar and harmonious. ',
'16. We are compatible with my spouse about what love should be. ',
'17. We share the same views about being happy in our life with my spouse ',
'18. My spouse and I have similar ideas about how marriage should be ',
'19. My spouse and I have similar ideas about how roles should be in marriage ',
'20. My spouse and I have similar values in trust. ',
'21. I know exactly what my wife likes. ',
'22. I know how my spouse wants to be taken care of when she/he sick. ',
'23. I know my spouses favorite food. ',
'24. I can tell you what kind of stress my spouse is facing in her/his life. ',
'25. I have knowledge of my spouses inner world. ',
'26. I know my spouses basic anxieties. ',
'27. I know what my spouses current sources of stress are. ',
'28. I know my spouses hopes and wishes. ',
'29. I know my spouse very well. ',
'30. I know my spouses friends and their social relationships. ',
'31. I feel aggressive when I argue with my spouse. ',
'32. When discussing with my spouse, I usually use expressions such as ‘you always’ or ‘you never’ . ',
'33. I can use negative statements about my spouses personality during our discussions. ',
'34. I can use offensive expressions during our discussions. ', 
'35. I can insult my spouse during our discussions.',
'36. I can be humiliating when we discussions. ',
'37. My discussion with my spouse is not calm. ',
'38. I hate my spouses way of open a subject. ',
'39. Our discussions often occur suddenly. ',
'40. We are just starting a discussion before I know whats going on. ',
'41. When I talk to my spouse about something, my calm suddenly breaks. ',
'42. When I argue with my spouse, ı only go out and I dont say a word. ', 
'43. I mostly stay silent to calm the environment a little bit. ',
'44. Sometimes I think its good for me to leave home for a while. ',
'45. I would rather stay silent than discuss with my spouse. ',
'46. Even if I am right in the discussion, I stay silent to hurt my spouse. ',
'47. When I discuss with my spouse, I stay silent because I am afraid of not being able to control my anger. ',
'48. I feel right in our discussions. ',
'49. I have nothing to do with what Ihave been accused of. ',
'50. I am not actually the one who is guilty about what I am accused of. ',
'51. I am not the one who is wrong about problems at home. ',
'52. I would not hesitate to tell my spouse about her/his inadequacy. ',
'53. When I discuss, I remind my spouse of her/his inadequacy. ',
'54. I am not afraid to tell my spouse about her/his incompetence. ']             

questionresults = []
resultweights= coef

print('PLEASE ANSWER THE FOLLOWING QUESTIONAIRE ')
print('THE ANSWER MUST BE A NUMBER BETWEEN 0 AND 4')
print('0 being "TOTALLY DISAGREE" and 4 being "TOTALLY AGREE" ')


for i in questionaire:
	print(i)
	res = float(input())
	questionresults.append(res)
	

multiplication = []

for num1, num2 in zip(questionresults, resultweights):
	multiplication.append(num1 * num2)

finalvalue = sum(multiplication)
result = 1.0 / (1.0 + exp(-finalvalue))
#print(result)
#print(round(result))
if(round(result) == 1):
	print('Couples with similar results tend to work out their differences with the help of counseling')
	print('If you work toghether you will get through this!!')
	
	
else:
		print('Couples with similar results tend to part ways. ')
		print('Sorry bro :(')