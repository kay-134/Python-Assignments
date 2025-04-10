##importing libraries/modules
import math

###Exercise 1##########################################################
#Write a function that takes a series of lists with infomation about multiple teams

#each list for each team is structured with the name, wins, losses and ties
input_data = [['Mets',10,5,5], ['Yankees',11,2,2], ['Bears',7,15,0], ['Senators',5,30,1], ['Clowns',10,50,1]]

def score(team_list):
    #a new list to hold the team name and score based on the calculation 
    score_list = []

    #a variable to hold the name of the team
    name = team_list[0]

    #adding the team name to the new list
    score_list.append(name)
    
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
    score_list.append(calculated_score)

   

    

    return score_list

def sort(teams):
    teams_to_sort = []
    new = []
    
    for team in teams:
        scored_team = [score(team)]
        teams_to_sort.append(scored_team)
        
    teams_to_sort.sort()
    teams_to_sort.reverse()

    for team in teams_to_sort:
        new.append(team.reverse())
        
    
    return(teams_to_sort)

print(sort(input_data))
        
    
