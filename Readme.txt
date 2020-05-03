--------------------------------------------------------------------------------------

Name : Siddharth Nahar
Entry No : 2016csb1043
Date : 21/4/20

---------------------------------------------------------------------------------------

* To Run the code

python main.py -p $(PROBLEM_ID) -f $(File_to_be_inputed)

Examples.

python main.py -p 4 -f Problem4/Test_Cases/strategic_info2.ini

-- Above runs 4th problem with specified file as input.

python main.py -p 1 -f Problem1/Test_Cases/strategic_info1.ini

-- Above runs 1st problem with specified file.

---------------------------------------------------------------------------------------

* Folder Structure

-- Folder consists of Problem1,2,3,4, main.py and Readme. Each Problem is appended by it's number.
-- Test case files for each Probelm is in its respective folder/Test_Cases
-- Code for each problem is under respective folder/analyse_equilibrium.py
-- Implementation details is under respective folder/Implementation_details.txt

---------------------------------------------------------------------------------------

* How Strategic Form game will be inputed ?

    -   It will be inputed as initialisation file as key value pair.
    
    -   File will contain two section. First section defines number of players and their strategies.
        Next section will contain utilities of indivisual players.

    -   There will be nested list of utilities. For s_i there will be single line of utility for all s_(-i). 
        Ordering will be fixed according to players and strategies as provided in file 1.

        Suppose 3 player game strategic form game

        [Strategies]
        N = 3
        Player1 = [a1, a2, a3]
        Player2 = [b1, b2, b3]
        Player3 = [c1, c2]
        
        [Utilities]
        Player1 = [
        [2, 3, 4, 5, 6, 7],    --> (For a1)(a1, b1, c1), (a1, b1, c2), (a1, b2, c1)......
        [1, 2, 3, 4, 5, 6],    --> (For a2)
        [0, 2, 3, 4, 5, 1]]

        Player2 = [
        [0, 1, 2, 3, 4, 1],    --> (For b1)(a1, b1, c1), (a1, b1, c2), (a2,b1,c1), (a2, b1, c2)......
        [1, 2, 3, 4, 5, 6],    --> (For b2)
        [1, 2, 3, 4, 5, 6]]

        Player3 = [ 
        [1, 2, 3, 4, 5, 6, 7, 8, 9], --->(For c1) (a1,  b1, c1), (a1, b2,c1), (a1, b3, c1), (a2, b1, c1) .......
        [0, 2, -4, -2, -1, -4, -5, -6, 1]]


--------------------------------------------------------------------------------------------
