##importing libraries/modules
import math
import turtle
import random

###Exercise 1##########################################################
#Write a function that takes a series of lists with infomation about multiple teams

#each list for each team is structured with the name, wins, losses and ties
input_data = [['Mets',10,5,5], ['Yankees',11,2,2], ['Bears',7,15,0], ['Senators',5,30,1], ['Clowns',10,50,1]]

def score(team_list):
    #a new list to hold the team name and score based on the calculation 
    score = 0

    name = team_list[0]
    
    #a variable to hold the amount of wins of a team
    wins = team_list[1]

    #a variable to hold the amount of losses of a team
    losses = team_list[2]

    #a variable to hold the amount of ties a team has
    ties = team_list[3]

    #a variable to hold the total number of games
    total_number_of_games = wins + losses + ties

    #a variable to hold the value of the calculated score
    calculated_score = (wins + (1/2  * ties))/total_number_of_games
    
    #adding the calculated score to the score list
    score = calculated_score

    #returns the score
    return score

#a function to sort the teams by score
def sort(teams):

    #a list to hold the order of the list
    teams_to_sort = []

    #for each list of teams in the list of teams
    for team in teams:

        #a variable holds the score of the team
        scored_team = [score(team)]

        #a list is created to hold the values of the score and the name (with the score forst so it can be sorted
        teams_to_sort.append([score(team), team[0] ])
       
        
    #the list is sorted by the score lowest to highest
    teams_to_sort.sort()

    #the order is reversed to highest to lowest
    teams_to_sort.reverse()

    #the team names and scores are printed in order of name then score
    for t in teams_to_sort:
        print(t[1] + ": " + str(t[0]))
    
#the function sort is called to sort the teams
sort(input_data)
        
    
###Exercise 2##########################################################
#Write a turtle graphics program that given 2 sets of coordinates will draw a complete bipartite graph.
#the two lists of coordinates
coord_list_1 = [[-200,200],[-200,90],[-50,-20]]
coord_list_2 = [[50,200],[50,170],[300,90],[50,30],[50,0],[50,-13],[50,-73]]

#a function to create the bipartite_graph
def bipartite_graph(list_1, list_2):

    #for each point in the forst list
    for point in list_1:

        #for each point in the second list
        for other_point in list_2:

            #each point in the first list is drawn to a point in the second list
            turtle.penup()

            #goes to a point from the first list
            turtle.setposition(point[0],point[1])

            #draws from the forst point to the second point
            turtle.pendown()
            turtle.setposition(other_point[0],other_point[1])

#running the list with the the sample coordinate lists inputted
bipartite_graph(coord_list_1, coord_list_2)


###Exercise 3##########################################################
