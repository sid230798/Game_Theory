## This will be driver for the evaluating games.
import argparse
from Utils.strategic_game_processing import create_startegic_game
from Utils.mechanism_design_processing import create_mechanism_design_problem
from Problem1.analyse_equilibrium import analyse as nash_equilibrium
from Problem2.analyse_equilibrium import analyse as mixed_nash_equilibrium
from Problem3.analyse_equilibrium import analyse as zeros_sum_game
from Problem4.analyse_equilibrium import analyse as Mech_Analyse

parser = argparse.ArgumentParser(description='Analysing different Games using tools from Game Theory')
parser.add_argument('-p', '--problem', type=int, choices=range(1, 5), required=True,\
                    help="Input the type of problem to analyse")
parser.add_argument('-f', '--file', required=True,\
                    help="Input initialisation file having all information regarding the game")

args = parser.parse_args()
problem_id = args.problem
init_file = args.file

if problem_id == 4 :
    n_players, type_set, type_index_set, outcomes, utility_set = create_mechanism_design_problem(init_file)
    Mech_Analyse(n_players, type_set, type_index_set, outcomes, utility_set)
else :
    N, startegies, utilities = create_startegic_game(init_file, problem_id)
    if problem_id == 1 :
        nash_equilibrium(startegies, utilities)
    elif problem_id == 2 :
        mixed_nash_equilibrium(startegies, utilities)
    else :
        zeros_sum_game(startegies, utilities)