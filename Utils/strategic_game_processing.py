## This file will be used to preprocess ini files
## This will generate the utility matrix for indivisual and Strategic space

from configparser import ConfigParser
import numpy as np
import ast

## This will parse utility matrix in same shape for all players
def parse_utility_matrix(index, utility_matrix, n_strategies_list) :
    
    ## This will create matrix of same shape but for different players
    for _ in range(2, len(n_strategies_list)) :
        utility_matrix = np.expand_dims(utility_matrix, axis=0)
    
    utility_matrix = np.reshape(utility_matrix, n_strategies_list)
    utility_matrix = np.moveaxis(utility_matrix, source=0, destination=index)
    return utility_matrix

## Parse ini file according to conventions
def create_startegic_game(init_file, problem_id) :

    config = ConfigParser()
    config.read(init_file)
    ## Get number of players
    n_players = config.getint('Strategies', 'N')
    strategies_list = list()
    n_strategies_list = list()
    utility_matrix_list = list()

    ## Get list of strategies for each player
    for index in range(1, n_players+1) :
        
        key = 'Player' + str(index)
        action_list = ast.literal_eval(config.get('Strategies', key))
        strategies_list.append(action_list)
        n_strategies_list.append(len(action_list))

    ## Get utility matrix for each player
    for index, (key, matrix) in enumerate(config.items('Utilities')) :
        
        utility_mat = ast.literal_eval(matrix)
        strats_list = n_strategies_list.copy()
        strats_list.insert(0, strats_list.pop(index))
        utility_matrix_list.append(parse_utility_matrix(index, utility_mat, strats_list))


    return n_players, strategies_list, utility_matrix_list

if __name__ == '__main__' :
    file_path = "../Test_Cases/Problem1/Test_Case1/strategic_info.ini"
    N, strats, utility = create_startegic_game(file_path, 1)
    print("Numbr of Playeers : ", N)
    print("Strategies : ",strats)
    print("Utility : ", utility)
