#function to toss the coin
def toss(coin):
    from random import shuffle
    shuffle(coin)
    return coin

# function to take the user input of names of players
# markers of players are given
# toss takes place by taking the h/t choice from player 1
def names_input():
    per1 = input('First Person Name : ').capitalize()
    per2 = input('Second Person Name : ').capitalize()
    m1='X'
    m2='O'
    print('')
    print(f'Hey {per1}, {m1} is your marker in the game')
    print(f'and {per2}, {m2} is your marker in the game')
    print('')
    print('Lets go for toss')
    print('')
    choice=input(f'Hey {per1} Heads or Tails? Just press H for heads and T for tails: ').upper()
    print('')
    coin=['H','T']
    coin=toss(coin)
    if coin[0] == choice:
        print(f'{per1} won the toss')
    else:
        print(f'{per2} won the toss')
        per1, per2 = per2, per1
        m1, m2= m2, m1
    pers=[]
    marks=[]
    pers.append(per1)
    pers.append(per2)
    marks.append(m1)
    marks.append(m2)
    return pers, marks
    
#function to create an array with empty spaces
def table_creation():
    x=[]
    for i in range(10):
        x.append(' ')
    return x
# function to clear the board
def clear_table(x):
    for i in range(9):
        x[i]=' '
    x[9]='just'
        
# function to display the board after every input from user
def display(x,sym,pos):
    x[pos-1] = sym
    print('-'*19)
    print(f'|  {x[6]}  |'+f'  {x[7]}  '+f'|  {x[8]}  |')
    print('-'*19)
    print(f'|  {x[3]}  |'+f'  {x[4]}  '+f'|  {x[5]}  |')
    print('-'*19)
    print(f'|  {x[0]}  |'+f'  {x[1]}  '+f'|  {x[2]}  |')
    print('-'*19)

#function which just displays the current board
def justdisplay(x):
    print('-'*19)
    print(f'|  {x[6]}  |'+f'  {x[7]}  '+f'|  {x[8]}  |')
    print('-'*19)
    print(f'|  {x[3]}  |'+f'  {x[4]}  '+f'|  {x[5]}  |')
    print('-'*19)
    print(f'|  {x[0]}  |'+f'  {x[1]}  '+f'|  {x[2]}  |')
    print('-'*19)

#function to display the board with their indices to give an idea to the player about the positions
def displayindex(x):
    print('-'*19)
    print('|  7  |  8  |  9  |')
    print('-'*19)
    print('|  4  |  5  |  6  |')
    print('-'*19)
    print('|  1  |  2  |  3  |')
    print('-'*19)

#function to instruct the players about board and its indices
def instruction(x):
    clear_table(x)
    print('This is the Tic Tac Toe Board')
    justdisplay(x)
    print('Remember the indices of the boxes')
    displayindex(x)

# function to take the postion input from user and validating it with few conditions
def position_input(x,per):
    ch='wrong'
    emp=' '
    while (not (ch.isdigit())) or int(ch) not in range(1,10) or x[int(ch)-1]!=' ':
        if emp in x:
            ch=str(input(f"It's your turn {per}: "))
            if not ch.isdigit():
                print('Please give a number as your choice')
            elif int(ch) not in range(1,10):
                print('Sorry, Invalid Input. Choose a number between 1 and 9')
            elif x[int(ch)-1]!=' ':
                print('Sorry, the box is already filled. Give the right choice')
        else:
            return 'null'
    
    return int(ch)

#function which runs the game 
def gaming(x,pers,marks):
    clear_table(x)
    
    emp=' '
    while emp in x:
        for i in range(2):
            choice=position_input(x,pers[i])

            if choice!= 'null':
                display(x,marks[i],choice)
                result=check_win(x,marks[i])
                if result:
                    return True, pers[i]
            else: 
                break          
    else:
        return False, 'Sorry'

# function to check winnning of any player
def check_win(x,m):
    z=0
    for z in range(0,7,3):
        if x[z:z+3].count(m) == 3:
            return True
    z=0
    for z in range(3):
        if x[z:z+7:3].count(m) == 3:
            return True
    z=0
    if x[z:z+9:4].count(m) == 3:
            return True
    z=2
    if x[z:z+5:2].count(m) == 3:
            return True
    return False

# function which gives output to user about win or draw
def go_for_game(x,pers,marks):
    res,person=gaming(x,pers,marks)
    if res:
        print(f'Congratulations {person}, you WON the game')
        game_on(x)
    else:
        print('All boxes are filled. GAME DRAW')
        justdisplay(x)
        game_on(x)

#function to ask the player about playing the game again
def game_on(x):
    print('')
    game_choice=input('Do you want play again? --- Y or N ? :').upper()
    if game_choice =='Y' or game_choice =='YES':

        lets_play()
    else:
        print('Thanks for Playing. Hope you enjoyed. Bye')
    
#the main function where everything starts
def lets_play():
    x=table_creation()
    pers,marks=names_input()
    instruction(x)
    go_for_game(x,pers,marks)

lets_play()