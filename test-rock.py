# Import the choice function of the random module
# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
import random

# Assign to a list the 3 possible options: 'stone', 'paper' or 'scissors'.
options=['stone','paper','scissors']

# Assign a variable to the maximum number of games: 1, 3, 5, etc ...
numberofgames=5

# Assign a variable to the number of games a player must win to win.
# Preferably the value will be based on the number of maximum games
winwin=3

# Define a function that randomly returns one of the 3 options.
# This will correspond to the play of the machine. Totally random.
def random_results():
    rs = random.choice(options)
    return rs

# Define a function that asks your choice: 'stone', 'paper' or 'scissors'
# you should only allow one of the 3 options. This is defensive programming.
# If it is not stone, paper or scissors keep asking until it is.
def ask_result():
    while True:
        option = input("Enter an option: ")
        if option in options:
            return option
            break
        else:
            print("Sorry,you must enter a valid option")
            continue


# Define a function that resolves a combat.
# Returns 0 if there is a tie, 1 if the machine wins, 2 if the human player wins
def combat(mc,hc):
    m = mc
    h = hc
    point_human=0
    point_machine=0
    if m==h:
        point_machine+=0
    elif m=="stone" and h=="scissors":
        point_machine+=1
    elif m=="paper" and h=="rock":
        point_machine+=1
    elif m=="scissors" and h=="paper":
        point_machine+=1
    else:
        point_human+=1

    results = (point_machine-point_human)
    
    if results == 0:
        print("0")
    elif results > 0:
        print("1")
    else:
        print("2")


mc=random_results()
hc=ask_result()
combat(mc,hc)

    
# Define a function that shows the choice of each player and the state of the game
# This function should be used every time accumulated points are updated
def combat_s(mc,hc):
    m = mc
    print("Machine choice",m)
    h = hc
    print("Human choice",h)
    point_human=0
    point_machine=0
    if m==h:
        point_machine+=0
    elif m=="stone" and h=="scissors":
        point_machine+=1
    elif m=="paper" and h=="rock":
        point_machine+=1
    elif m=="scissors" and h=="paper":
        point_machine+=1
    else:
        point_human+=1

    results = (point_machine-point_human)
    
    if results == 0:
        print("0")
    elif results > 0:
        print("1")
    else:
        print("2")
        
mcs=random_results()
hcs=ask_result()
combat_s(mcs,hcs)

# Create two variables that accumulate the wins of each participant
def combat_acu(mc,hc):
    m = mc
    print("Machine choice",m)
    h = hc
    print("Human choice",h)
    point_human=0
    point_machine=0
    if m==h:
        point_machine+=0
    elif m=="stone" and h=="scissors":
        point_machine+=1
    elif m=="paper" and h=="rock":
        point_machine+=1
    elif m=="scissors" and h=="paper":
        point_machine+=1
    else:
        point_human+=1

    results = (point_machine-point_human)
    
    if results == 0:
        print("0")
    elif results > 0:
        print("1")
    else:
        print("2")

# Create a loop that iterates while no player reaches the minimum of wins
def combat_acu_min(mc,hc,n):
    m = mc
    print("Machine choice",m)
    h = hc
    nog = n
    print("Human choice",h)
    point_human=0
    point_machine=0  

    while point_human <= 5 or point_machine <=5:
        while True:
            if point_human >= nog:
                print("2")
                break
            elif point_machine >= nog:
                print("1")
                break
        else:
            if m==h:
                point_machine+=0
            elif m=="stone" and h=="scissors":
                point_machine+=1
            elif m=="paper" and h=="rock":
                point_machine+=1
            elif m=="scissors" and h=="paper":
                point_machine+=1
            else:
                point_human+=1
            results = (point_machine-point_human)

            continue

mcsa=random_results()
hcsa=ask_result()
combat_acu_min(mcsa,hcsa,numberofgames)

# necessary to win. Inside the loop solves the play of the
# machine and ask the player's. Compare them and update the value of the variables
# that accumulate the wins of each participant.

    
# Print by console the winner of the game based on who has more accumulated wins
  