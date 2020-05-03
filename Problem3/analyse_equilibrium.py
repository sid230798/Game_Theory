## This file will find out equilibriums for two player zero sum game.
import numpy as np
from scipy.optimize import linprog

## Calculate saddle point in matrix a
def saddle_point(strategies, a) :

    min_vals = np.amin(a, axis=1)
    max_vals = np.amax(a, axis=0)
    maxmin = np.max(min_vals)
    minmax = np.min(max_vals)

    if maxmin != minmax :
        print("No saddle point exists.............")
    else :
        
        saddle_points = "{"
        indices = np.argwhere(a == maxmin)
        for row in indices :
            saddle_points += "(" + str(row[0]+1) + "," +str(row[1]+1) + ")"
        
        saddle_points += "}"
        print("Saddle points are : ", saddle_points)

## Calculate MSNE for Zero sum game
def msne(strategies, a) :

    ## One zero array for later (z, x)
    ess = np.ones(a.shape[0]+1)
    ess[0] = 0

    c = -1*(1-ess)  ##[-1, 0 ,0 ,0] -1 coeff for z and 0 for x (Max z == min(-z))
    A_ub = np.concatenate((np.ones((1, a.shape[1])), -1*a), axis=0).T
    B_ub = np.zeros(a.shape[1])
    A_eq = np.expand_dims(ess, axis=0)
    B_eq = np.ones(1)
    bounds = [(None, None)] + [(0,1)]*a.shape[0]
    result = linprog(c, A_ub=A_ub, b_ub=B_ub, A_eq=A_eq, b_eq=B_eq, bounds=bounds)
    p1_val, p1_distribution = result.x[0], result.x[1:]

    ## For 2nd player distribution
    ess = np.ones(a.shape[1]+1)
    ess[0] = 0
    c = (1-ess)
    A_ub = np.concatenate((-1*np.ones((a.shape[0], 1)), a), axis=1)
    B_ub = np.zeros(a.shape[0])
    A_eq = np.expand_dims(ess, axis=0)
    A_eq = np.concatenate((A_eq, 1-A_eq), axis=0)
    B_eq = np.array([1, p1_val]) ## Dual Principle w* = z*
    bounds = [(None, None)] + [(0,1)]*a.shape[1]
    result = linprog(c, A_ub=A_ub, b_ub=B_ub, A_eq=A_eq, b_eq=B_eq, bounds=bounds)
    p2_val, p2_distribution = result.x[0], result.x[1:]

    print("MSNE are : {", tuple(p1_distribution), "," ,tuple(p2_distribution), "}")

def analyse(strategies, utilities) :

    saddle_point(strategies, utilities[0])
    msne(strategies, utilities[0])
