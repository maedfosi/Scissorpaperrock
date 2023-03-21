### this a beginners code to scissor, paper, rock game.

from random import randrange #Import module randrange

you = int(0) #Create two variables to count the wins.
machine = int(0)

moves = {1:"Scissor", 2:"Paper", 3:"Rock"} #Use a dictionary to clasified the options

print("Options: 1=Scissor, 2=Paper, 3=Rock") #Show the options to the player.

while you < 3 and machine < 3: #Now, we have to create a loop for the game        
        h = int(input("Make your selection (Choose a number): ")) #in this code we get the choose of user and the choose option of the machine with the randrange module.
        if h < 1 or h > 3:
            print("¡Hey! ¡Choose a option number!")
        else:
            my_move = moves.get(h)
            print("your move: ", my_move)
            for i in range(1):
                m = int(randrange(1,4))
                mach_move = moves.get(m)
                print("machine move: ", mach_move)
                
            if my_move == mach_move: #next, we going to compare the results and define the turn winner.
                    None
            elif my_move == moves.get(1) and mach_move == moves.get(2):
                    you += 1
            elif my_move == moves.get(1) and mach_move == moves.get(3):
                    machine += 1
            elif my_move == moves.get(2) and mach_move == moves.get(1):
                    machine += 1
            elif my_move == moves.get(2) and mach_move == moves.get(3):
                    you += 1
            elif my_move == moves.get(3) and mach_move == moves.get(1):
                    you += 1
            elif my_move == moves.get(3) and mach_move == moves.get(2):
                    machine += 1
            print("Your wins: ",you)
            print("Machine wins: ",machine)
else: #When a player reach 3 wins the game ends and print a message to player
    if you == 3:
        print("¡Aaaaaaaa you're the winner!")
    else:
        machine == 3
        print("¡Hahahahaha I'm the winner!")
