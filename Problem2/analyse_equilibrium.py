## This calculates msne for two player game
from itertools import chain, combinations, product
from scipy.optimize import linprog
import numpy as np

## We will apply Linear programming to analyse if delta_set has msne
def msne(delta_set, strategies, utilities) :
    
    # Solving for player one we will utilise probablities of player2
    # For Calculating probablities of second player2
    # Max u_1(s_1, sigma_i)......
    result_probablities = list()
    delta_strats = list()
    for index in range(len(delta_set)) :

        org_shape = utilities[index].shape
        utility_mat = np.moveaxis(utilities[index], source=index, destination=0)
        ## Slice utilites only present in delta set.
        delta_utilities = np.take(np.take(utility_mat, indices=delta_set[index], axis=0),\
                                    indices=delta_set[1-index], axis=1)
        ## Take utilities for other player index
        delta_utility_player = np.take(utility_mat, indices=delta_set[1-index], axis=1)
        c = -delta_utilities[0]
        A_ub = np.reshape(delta_utility_player[:, np.newaxis] - delta_utilities, (-1, len(delta_set[1-index])))
        B_ub = np.zeros(A_ub.shape[0])
        A_eq = np.ones((1, len(delta_set[1-index])))
        B_eq = np.ones(A_eq.shape[0])
        if len(delta_set[index]) > 1 :
            A_eq = np.concatenate((np.reshape(delta_utilities[:, np.newaxis] - delta_utilities,\
                                    (-1, len(delta_set[1-index]))), A_eq), axis=0)
            B_eq = np.concatenate((np.zeros(A_eq.shape[0]-1), B_eq))
        bounds = [(0.00000005, 1)]*len(delta_set[1-index])
        result = linprog(c, A_ub=A_ub, b_ub=B_ub, A_eq=A_eq, b_eq=B_eq, bounds=bounds)

        if result.status == 2 :
            return

        result_probablities = [result.x] + result_probablities
        delta_strats += [[ strategies[index][i] for i in delta_set[index] ]]
    
    print("Delta Sets and Probalities are : {", delta_strats[0], " : ", result_probablities[0],\
            ", ",delta_strats[1]," : ", result_probablities[1], "}")


def analyse(strategies, utilities) :

    ## Get two list of startegies and create powerset from it and its cartesian product.
    s0,s1 = range(len(strategies[0])), range(len(strategies[1]))
    powerset0 = chain.from_iterable(combinations(s0, r) for r in range(1, len(s0)+1))
    powerset1 = chain.from_iterable(combinations(s1, r) for r in range(1, len(s1)+1))
    
    print("All Mixed Strategies Equilibriums are  : \n")
    for delta_set in product(powerset0, powerset1) :
        msne(delta_set, strategies, utilities)