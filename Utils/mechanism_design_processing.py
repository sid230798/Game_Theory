## For processing of mechanism design processing.

from configparser import ConfigParser
import numpy as np
import ast

## Parse mechanism design file to get all values 
def create_mechanism_design_problem(init_file) :

    config = ConfigParser()
    config.read(init_file)

    n_players = config.getint('Players', 'N')
    outcomes = ast.literal_eval(config.get('Outcomes', 'Outcomes'))
    type_set = list()
    type_index_set = list()
    utility_set = list() ## This will contain utility of form (x, theta)

    ## Get indivisual type sets
    for key, types in config.items('TypeSet') :
        types = ast.literal_eval(types)
        type_set.append(types)
        type_index_set.append(list(range(len(types))))

    ## Get inidivisual utility matrix of x,theta
    for key, utility_mat in config.items('Utilities') :
        utility_mat = ast.literal_eval(utility_mat)
        mat = np.array(utility_mat).T
        utility_set.append(mat)

    return n_players, type_set, type_index_set, outcomes, utility_set

if __name__ == '__main__' :
    file_path = "../Problem4/Test_Case1/strategic_info.ini"
    N, type_set, type_index_set, outcomes, utility_set = create_mechanism_design_problem(file_path)
    print("Numbr of Playeers : ", N)
    print("Outcomes : ",outcomes)
    print("Type Sets : ", type_set)
    print("Utility Matrix", utility_set)