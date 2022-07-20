import random
A,B=0,0
restart="Yes"
def new(A,B):
    '''For restart, set up the score board again'''
    A=0
    B=0
    return A,B
def Rock(A,B,comp_choice):
    '''Checking the condition for rock'''
    if comp_choice=="Scissors":
        A+=1
    elif comp_choice=="Paper":
        B+=1
    return A,B
def Paper(A,B,comp_choice):
    '''Checking the condition for paper'''
    if comp_choice=="Scissors":
        B+=1
    elif comp_choice=="Rock":
        A+=1
    return A,B
def Scissors(A,B,comp_choice):
    '''Checking the condition for scissors'''
    if comp_choice=="Rock":
        B+=1
    elif comp_choice=="Paper":
        A+=1
    return A,B
def game(A,B,comp_choice,move):
    '''The moves are input, functions are accessed and scores are decided'''
    if move=='Scissors':
        A,B=Scissors(A,B,comp_choice)
    elif move=="Paper" :
        A,B=Paper(A,B,comp_choice)
    elif move=="Rock":
        A,B=Rock(A,B,comp_choice)
    else:
        print("Enter a valid choice")
    print("Player 1 chose: ", move)
    print("Player 2 chose: ", comp_choice)
    print("Player 1: ", A)
    print("Player 2: ", B)
    return A,B
def game_begins_1(A,B):
    '''The game starts and goes on till a winner is produced'''
    new(A,B)
    while A<5 and B<5:
        move=input("Make the move, rock, paper or scissors: ").title()
        c=["Rock","Paper","Scissors"]
        comp_choice=random.choice(c)
        A,B=game(A,B,comp_choice,move)
    if A==5: 
        print("Player One Wins!")
    elif B==5:
        print("Player Two wins! ")
while restart=="Yes":
    '''cause what if people wanna play again and again'''
    ok=input("1 Player or 2?")
    if ok=="1":
        game_begins_1(A,B)
        restart=input("Wanna Play again (Yes/No)").title()
    elif ok=="2":
        new(A,B)
        while A<5 and B<5:
            move=input("Make the move, Player 1: rock, paper or scissors: ").title()
            comp_choice=(input("Make the move, Player 2: rock, paper or scissors: ")).title()
            A,B=game(A,B,comp_choice,move)
        if A==5: 
            print("Player One Wins!")
        elif B==5:
            print("Player Two wins! ")
        restart=input("Wanna Play again (Yes/No)").title()
