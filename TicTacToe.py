# # Tictactoe in python by Savannah

game = [
    ['    ', '1', '2', '3'], [' A  ', '_', '_', '_'], [' B  ', '_', '_', '_'],
    [' C  ', '_', '_', '_']
]  # game board set up with 2D array using alpha/numeric coordinate system for marker placement
Xscoret= [0]  #setting temp score used to track marker counts for player one
Oscoret= [0]  #setting temp score used to track marker counts for player two
p1 = 'X'  #player one is X
p2 = 'O'  #player two is O
counter = 0  #counter counts each time a marker is placed. It used to determine player turn, to end game if player wins, also will determine if game is a tie i.e cats game.
def winning_statement(Xscoret, Oscoret, game, counter):
    if Xscoret[0]== len(game) - 1:
        print 'Player 1 wins'
        counter = len(game)**2
    if Oscoret[0]== len(game) - 1:
        print 'Player 2 wins'
        counter = len(game)**2
# def index_temp_score(game,row,column,Xscoret,Oscoret,test):
    
#     for elem in game[row][column]:
#         if elem == 'X':
#             Xscoret[0]= Xscoret[0]+ 1
#         if elem == 'O':
#             Oscoret[0]= Oscoret[0]+ 1
#         test += 1
#         print Xscoret
    #print test
    


def winner(game, Xscoret, Oscoret):  #function checks for winner by calculating a temp score. if temp score represents a winning solution (i.e. 3 in a row b1,b2,b3) a winner statement will be printed and counter will exceed the possible number of positions played thus ending while loop in tictactoe(game, Xscoret,Oscoret,select,p1,p2, counter)
   
    column = 1
    test = 0
    while column < len(game):  #checks columns for wins
        Oscoret[0]= 0
        Xscoret[0]= 0
        row = 1
        while row < len(game):
            index_temp_score(game,row,column,Xscoret,Oscoret,test)
            # for elem in game[row][column]:
            #     if elem == 'X':
            #         Xscoret[0]= Xscoret[0]+ 1
            #     if elem == 'O':
            #         Oscoret[0]= Oscoret[0]+ 1

            row = row + 1
            column = column + 1
        winning_statement(Xscoret, Oscoret, game, counter)
    row = 1
    while row < len(game):  #checks rows for wins
        Oscoret[0]= 0
        Xscoret[0]= 0
        column = 1
        while column < len(game):
            index_temp_score(game,row,column,Xscoret,Oscoret,test)
            # for elem in game[row][column]:
            #     if elem == 'X':
            #         Xscoret[0]= Xscoret[0]+ 1
            #     if elem == 'O':
            #         Oscoret[0]= Oscoret[0]+ 1
            column = column + 1
            row = row + 1
        winning_statement(Xscoret, Oscoret, game, counter)
    row = 1  #checks diagnal for wins right handed(ie a1,b2,c3)
    Oscoret[0]= 0
    Xscoret[0]= 0
    while row < len(game):
        column = row
        index_temp_score(game,row,column,Xscoret,Oscoret,test)
        # for elem in game[row][column]:
        #     if elem == 'X':
        #         Xscoret[0]= Xscoret[0]+ 1
        #     if elem == 'O':
        #         Oscoret[0]= Oscoret[0]+ 1
        row = row + 1
    winning_statement(Xscoret, Oscoret, game, counter)
    row = 1  #checks diagnal for wins left handed(ie a3,b2,c1)
    Oscoret[0]= 0
    Xscoret[0]= 0
    while row < len(game):
        index_temp_score(game,row,column,Xscoret,Oscoret,test)
        # for elem in game[row][column]:
        #     if elem == 'X':
        #         Xscoret[0]= Xscoret[0]+ 1
        #     if elem == 'O':
        #         Oscoret[0]= Oscoret[0]+ 1
        row = row + 1
        column = column - 1
    winning_statement(Xscoret, Oscoret, game, counter)
    


def select(game, row_pos, column_pos, player):
    game[row_pos][column_pos] = player
    # index fist row then columns to define player position


def print_game(game):
    print ''
    for row in game:
        print ' '.join(row)
    print ''


def marker_placement_pos(
        game):  #setting marker placement from player input of row,column
    
    #placement is a local variable used for flow control. Set to 0, 'ok', or 'invalid (1,2,or 3)'.  Vairiable is also used for narrowing which type of input error is cuasing issues during build. may not be required to in final product, adding invalid print statment for player information, which could also be used to track input errors.
    placement = 0  #placement = pre-set to 0 to start while loop

    while placement != 'ok':  #loop contructs valid marker placement through player input and feed back to prompt player for valid input in cases when input is invalid.
        pos = list(
            raw_input('Place your marker: ')
        )  #statment asking for player input for marker placement. player input is put into a list to allow split the input through indexing.
        row_temp = pos[0].upper(
        )  #sets row for marker placement and allows player input to be lowercase or upper case
        if row_temp == "Q":
            if player == "X":
                looser = "Player 1"
                winner = "Player 2" 
            else:
                looser = "Player 2"
                winner = "Player 1"
            print looser + " quit. " + winner + ", you win!"
            exit()
        try:
            column_temp = int(pos[1])  #sets column for marker placement.
        except ValueError:  #handles exception if player passes non-numeric value
            print "Sorry, invalid placement. Please check format."

        while placement != 'ok':  #loop checks player input is length 2 (Catches inputs that are blank or too long or too short)
            if len(pos) != 2:  #checks input for length of 2
                print "invalid placement input > 2"  #statement to inform player of reason for marker invalid placement
                placement = 'invalid (1)'  #placement set to invalid, continues loop until player inputs marker placement with length of two
            else:
                placement = 'ok'  #placement set to ok, condition for input marker placment of lenth two is met.

        placement = 0  #placement = pre-set to 0 to start while loop

        while placement != 'ok':  #loop checks row input as

            row_list = ['A', 'B', 'C']
            if row_temp in row_list:
                placement = 'ok'

                row_assign = {'A': 1, 'B': 2, 'C': 3}
                row_temp = row_assign.get(row_temp)

            else:
                print "invalid placement"
                placement = 'invalid (2)'

            if type(column_temp) != int or int(column_temp) > 3:
                print "invalid placement"
                placement = 'invalid (3)'
                exit()
            global row_pos
            row_pos = row_temp
            global column_pos
            column_pos = column_temp

            if column_pos < 4 and type(column_pos) == int:
                if game[row_pos][column_pos] != '_':
                    print "That's cheating;)"
                    placement = 'invalid'


def setup(game):
    print "Welcome to Tic-Tac-Toe! This is a two player game. Player 1, you are X. Player 2, you are O. First to place their marker three in a row wins!"
    print_game(game)
    print "Place your marker by selecting row then column. For example A3 will place a marker here:"
    select(game, 1, 3, 'X')
    print_game(game)
    print ''
    print ''
    print ''
    select(game, 1, 3, '_') 
    print "  let's play!     (use Q to quit)"    
    print_game(game)


def tictactoe(game, Xscoret, Oscoret, select, p1, p2, counter):
    setup(game)
    counter = 0
    while counter < ((len(game) - 1)**2):
        if counter % 2 == 0:
            global player
            player = p1
            print "!!!~~~~~Player 1~~~~~!!!"
        else:
            player = p2
            print "!!!~~~~~Player 2~~~~~!!!"
        marker_placement_pos(game)
        select(game, row_pos, column_pos, player)
        print_game(game)
        winner(game, Xscoret, Oscoret)
        counter = counter + 1
        print counter
    if counter < (len(game)**2):
        print "Cat's game. Tie"


tictactoe(game, Xscoret, Oscoret, select, p1, p2, counter)
