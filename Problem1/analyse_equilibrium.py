## This file contains calculate basic equilibriums
import numpy as np

## This Prints all dominant startegies for each player
def strongly_dominant_strategies(strategies, utilites) :

    sds = list()
    ## Iterate for each player to calculate SDSE
    for index in range(len(strategies)) :

        # Get max index of si for all s_(-i)
        max_index = np.argmax(utilites[index], axis=index)
        max_val = np.max(max_index)
        ## If all index values are same then its a possible candidate
        if np.all(max_index == max_val) :
            ## To check if s_i > s_i' for all s_(-i)
            values = np.max(utilites[index], axis=index)
            values = np.expand_dims(values, axis=index)
            values = np.repeat(values, len(strategies[index]), axis=index)
            sub_mat = values - utilites[index]
            sub_mat = np.delete(sub_mat, max_val, axis=index)
            if np.all(sub_mat > 0) :
                sds.append(max_val)
            else :
                sds.append(-1)
        else :
            sds.append(-1)

    # Enumerate SDS for all players
    print("Strongly Dominant Startegies are : ")
    isSDSE = True
    for idx, index in enumerate(sds) :
        if index == -1 :
            print("Player", idx+1, " : No Dominant Startegy")
            isSDSE = False
        else :
            print("Player", idx+1, " : ",strategies[idx][index], " is a Strongly Dominant Startegy")
    print("------------------------------------------")
    return sds, isSDSE

## Prints all Weakly dominant startegies
def weakly_dominant_startegies(strategies, utilites) :
    
    wds = list()
    ## Iterate through indivisual strategy for wds
    for index in range(len(strategies)) :
        ## As Weakly dominant startegies follows >= rule we need to get each and every
        ## index where max value occurs
        max_vals = np.max(utilites[index], axis=index)
        max_vals = np.expand_dims(max_vals, axis=index)
        all_indices = np.argwhere(utilites[index] == max_vals)
        ## All indices n*Total_Players
        axis_indices = np.take(all_indices, indices=index, axis=1)
        idx, counts = np.unique(axis_indices, return_counts=True)
        ## Check if max val counts are equal to number of s_i
        if np.max(counts) == np.prod(np.shape(max_vals)) :
            ## Check if there are no two such strategies
            if len(np.argwhere(counts == np.max(counts))) > 1 :
                wds.append(-1)
            else :
                wds.append(idx[np.argmax(counts)])
        else :
            wds.append(-1)

    ## Enumerate all WDS for all Players
    print("Weakly Dominant Startegies are : ")
    isWDSE = True
    for idx, index in enumerate(wds) :
        if index == -1 :
            print("Player", idx+1, " : No Dominant Startegy")
            isWDSE = False
        else :
            print("Player", idx+1, " : ",strategies[idx][index], " is a Weakly Dominant Startegy")
    print("------------------------------------------")
    return wds, isWDSE

## Prints SDSE and WDSE
def print_equilibrium(strategies, idx_list) :

    equil_strats = "{"
    for idx, index in enumerate(idx_list) :
        equil_strats += strategies[idx][index]
        equil_strats += ", "
    
    equil_strats = equil_strats[:-2] + "}"
    return equil_strats

## Print Nash Equilibriums
def nash_equilibrium(strategies, utilites) :
    
    indices_max = list()
    ## Get max s_i for all S_-i for all i's. If that array intersect each other we have PSNE.
    for index in range(len(strategies)) :
        max_vals = np.max(utilites[index], axis=index)
        max_vals = np.expand_dims(max_vals, axis=index)
        all_indices = np.array(np.argwhere(utilites[index] == max_vals).tolist())
        dtypes = 'int64, '*all_indices.shape[1]
        all_indices = all_indices.view(dtypes[:-2])
        indices_max.append(all_indices)

    ## Get intersection of arrays
    intersect_f = indices_max[0]
    for index in range(1, len(indices_max)) :
        intersect_f = np.intersect1d(intersect_f, indices_max[index])

    print("Nash Equilbriums are : ")    
    for index, row in enumerate(intersect_f) :
        print(index+1, ". ", print_equilibrium(strategies, row))
    
    if len(intersect_f) == 0 :
        print("No nash equilibriums.............")
    
    print("-----------------------------------------")

## Maxmin values and their Strategies
def maxmin(strategies, utilites) :

    axis_list = list(range(len(strategies)))
    for index in range(len(strategies)) :
        # Get min across all axis and its max val
        axis_tuple = tuple(axis_list[:index] + axis_list[index+1:])
        min_vals = np.amin(utilites[index], axis=axis_tuple)
        maxminval = np.max(min_vals)
        maxminstrats = np.argwhere(min_vals == maxminval).flatten()
        print("Maxmin Value for Player",index+1," : ", maxminval)
        starts_list = "{"
        for idx in maxminstrats :
            starts_list += strategies[index][idx] + ","
        starts_list = starts_list[:-1] + "}"
        print("MaxMin Strategies for Player",index+1," are : ",starts_list)

    print("-----------------------------------------")

## Minimax Value and Startegies of other player
def minmax(strategies, utilites) :

    for index in range(len(strategies)) :
        # Get max across s_i and min across rest of it.
        max_vals = np.amax(utilites[index], axis=index)
        minmaxval = np.min(max_vals)
        minmaxstrats = np.argwhere(max_vals == minmaxval)
        print("Minmax Value for Player",index+1," : ",minmaxval)
        starts_list = "{"
        for row in minmaxstrats:
            indivisual_list="("
            forloopCount = 0
            for idx in range(len(strategies)) :
                if idx == index :
                    continue
                indivisual_list += strategies[idx][row[forloopCount]] + ","
                forloopCount += 1
            indivisual_list = indivisual_list[:-1] + ")"
            starts_list += indivisual_list + ","

        starts_list = starts_list[:-1] + "}"
        print("MinMax Startegies against Player",index+1," are : ",starts_list) 

    print("-----------------------------------------")

def analyse(strategies, utilites) :

    sds, isSDSE = strongly_dominant_strategies(strategies, utilites)
    wds, isWDSE = weakly_dominant_startegies(strategies, utilites)
    if isSDSE :
        print("Strongly Dominant Strategy Equilibrium is : ", print_equilibrium(strategies, sds))
    else :
        print("No SDSE")
    
    print("-----------------------------------------")
    
    if isWDSE :
        print("Weakly Dominant Strategy equilibrium is : ", print_equilibrium(strategies, wds))
    else :
        print("No WDSE")

    print("-----------------------------------------")

    nash_equilibrium(strategies, utilites)
    maxmin(strategies, utilites)
    minmax(strategies, utilites)