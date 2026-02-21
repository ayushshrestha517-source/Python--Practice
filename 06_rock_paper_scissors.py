import random
'''
1 for Rock
0 for Paper
-1 for Scissors
'''
print("ROCK ! PAPER ! SCISSORS !")
print("==Game START==")

player_dict = {
    "rock":1,
    "paper":0,
    "scissors":-1
}

game_dict = {
    1:"Rock",
    0:"Paper",
    -1:"Scissors"
}

while True:
    computer = random.choice([-1,0,1])
    while True:
        playerstr = input("Enter your choice: ").strip().lower()
        if playerstr in ("rock","paper","scissors"):
            break
        else:
            print("Mistake in entering choices. Please Enter valid choices!")

    player= player_dict[playerstr]

    print (f"Computer chose: {game_dict[computer]}\nPlayer chose: {game_dict[player]}")

    '''
    Determine the winner:
    Player wins if (computer - player) == 1 or (computer - player) == -2
        Examples of player wins with current mapping (1=Rock, 0=Paper, -1=Scissors):
            1) computer=Rock(1), player=Paper(0)      -> 1-0 = 1        //Player wins
            2) computer=Paper(0), player=Scissors(-1) -> 0-(-1) = 1     //Player wins
            3) computer=Scissors(-1), player=Rock(1)  -> -1-1 = -2      //Player wins
    Draw if computer == player
    Otherwise, player loses
    '''

    if((computer-player)==1 or (computer-player)==-2):
        print("Player Win!")
        
    elif(computer==player):
        print("It's a Draw...")

    else:
        print("Player Lost!")

    # Ask if player wants to continue
    while True: 
        ch = input("Do you want to continue playing the game?(yes/no): ").strip().lower()
        if ch in ("yes","no"):
            break
        else:
            print("Please enter either yes or no.")
    if ch == "no":
        print("Exited the game, Thank You!")
        break