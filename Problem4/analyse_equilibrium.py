## This contains algorithm to check if social choice function is
## DSIC, ex-post efficient and non-dictatorial
import numpy as np
from itertools import product

def seeDSIC(scf, types_total, utility_set) :

    for index, value in enumerate(types_total) :

        new_shape = tuple(types_total) + tuple([value])
        ## Change utility in format Theta1, theta2, theta3..., Theta1
        mat = np.take(utility_set[index], indices=scf, axis=0)
        mat = np.reshape(mat, new_shape)
        for idx in range(value) :
            for_theta_idx = np.take(mat, indices=idx, axis=-1)
            for_theta_idx = np.moveaxis(for_theta_idx, source=index, destination=0)
            for_theta_idx = np.reshape(for_theta_idx, (value, -1))
            diag_val = for_theta_idx[idx]
            if not np.all(for_theta_idx - diag_val <= 0) :
                return False
    return True

## For ex-post-effcient
def ex_post(type_cartesian_product, scf, utility_set) :
    
    for f_theta, theta in zip(scf, type_cartesian_product) :
        
        outcome_index_list = list()
        ## Get indices off all players where outcome is greater then f_theta
        for index, utility_mat in enumerate(utility_set) :
            utility_theta = np.take(utility_mat, theta[index], axis=1)
            u_f_theta = np.squeeze(np.argwhere(utility_theta >= utility_theta[f_theta]), axis=1)
            u_f_theta = u_f_theta[u_f_theta != f_theta]
            outcome_index_list.append(u_f_theta)
        
        ## Get intersection of those indices
        final_index = outcome_index_list[0]
        for indices in outcome_index_list[1:] :
            final_index = np.intersect1d(final_index, indices)
        
        ## Check if any indice has greater value
        if len(final_index) > 0 :
            for index, utility_mat in enumerate(utility_set) :
                utility_theta = np.take(utility_mat, theta[index], axis=1)
                f_theta_val = utility_theta[f_theta]
                final_index_val = np.take(utility_theta, final_index)
                if len(np.argwhere(final_index_val > f_theta_val)) > 0 :
                    return False

    return True    

## Check if scf is dicatorial
def non_dicatorial(type_cartesian_product, scf, utility_set) :

    for index, utility_mat in enumerate(utility_set) :
        player_indices = [ theta[index] for theta in type_cartesian_product ]
        max_vals = np.max(utility_mat, axis=0)
        f_theta_vals = np.array([ utility_mat[f][t] for f,t in zip(scf, player_indices) ])
        extend_max_vals = np.take(max_vals, player_indices)
        if np.array_equal(f_theta_vals, extend_max_vals) :
            return False
    
    return True

def printSCF(scf, type_cartesian_product, type_set, outcomes) :

    scf_str = ""
    for outcome, theta in zip(scf, type_cartesian_product) :
        theta_str = "f("
        for index, idx in enumerate(theta):
            theta_str += type_set[index][idx] + ", "
        
        theta_str = theta_str[:-2] + ") = " + outcomes[outcome]
        scf_str += theta_str + ", "

    print(scf_str[:-2])

    pass

def analyse(N, type_set, type_index_set, outcomes, utility_set) :

    type_cartesian_product = list(product(*type_index_set, repeat=1))
    n_possible_scf = len(outcomes)**len(type_cartesian_product)
    all_possible_permute_outcomes = product(list(range(len(outcomes))), repeat=len(type_cartesian_product))
    types_total = [len(type_indi) for type_indi in type_set]    
    
    print("All possible SCF with properties given are : \n")
    isPoss = False
    for index, scf in enumerate(all_possible_permute_outcomes) :
    
        if  ex_post(type_cartesian_product, scf, utility_set) and\
            seeDSIC(scf, types_total, utility_set) and\
            non_dicatorial(type_cartesian_product, scf, utility_set) :

            printSCF(scf, type_cartesian_product, type_set, outcomes)
            isPoss = True
        
    if not isPoss :
        print("No such Possible SCF's .......................")