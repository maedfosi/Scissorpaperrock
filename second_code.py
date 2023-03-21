from random import randrange #Import module randrange

def ask(): # A function to know if the user wants to play
    play = input("Do you wanna play?: Y / N ")
    decision(play)
    
def decision(play): # A function to send a message to user depends of his answer
    if play == "Y":
        start_game(play)
    elif play == "N":
        print("Ok, bye")
    else:
        print('I don\'t get it!')
        ask()

def start_game(Y): #The function of the game
    you = 0 #Create two variables to count the wins.
    machine = 0
    moves = {1:"Scissor", 2:"Paper", 3:"Rock"} #Use a dictionary to clasified the options
    while you < 3 and machine < 3: #Now, we have to create a loop for the game  
        h = int (input("Make your selection (Chose a number): "))
        if h < 1 or h > 3:
            print("Hey! Choose a option number!")
        else:
            my_move = moves.get(h)
            print("your move: ", my_move)
            for i in range(1):
                m = int(randrange(1,4))
                mach_move = moves.get(m)
                print("machine move: ", mach_move)
            if my_move == mach_move: #In this part of the code reduce the number of lines, removing the option where the machine wins and just use a else.
                None
            elif my_move == moves.get(1) and mach_move == moves.get(2):
                you += 1
            elif my_move == moves.get(2) and mach_move == moves.get(3):
                you += 1
            elif my_move == moves.get(3) and mach_move == moves.get(1):
                you += 1
            else:
                machine += 1
            print("Your wins: ",you)
            print("Machine wins: ",machine)
        if you == 3: #Add this part of code to launch a respond acoording to the result.
            winner = you
            user_win(winner)
        elif machine == 3:
            winner = machine
            machine_win(winner)

def user_win(winner): #A function where the user wins.
    print("OMG! You're a great player!")
    ask()

def machine_win(winner): #A function where the machie win
    print("Ooohh! Best luck to the next time! cof cof... loser!")
    ask()

ask() #This function launch the question for the player.
