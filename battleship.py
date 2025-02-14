"""
    File: battleship.py
    
    Author: Yandi Xu
    
    Purpose: This program involves writing a program to model half of the
        actual board game, namely, Player 1's ship placements and Player 2's guesses.
       
"""

import sys

class GridPos:
    '''
    An instance of this class describes a grid position.

    Attributes: self._pos： the x- and y-coordinates of the position.

                self._ship： the Ship object at this position, if not None.

                self._guessed： whether or not it has been previously guessed.    
    '''
    def __init__(self, x, y):
        self._pos  = (x, y)
        self._ship = None
        self._guessed = False

    def get_position(self):
        '''return the position'''
        return self._posi

    def get_ship(self):
        '''return the Ship object'''
        return self._ship

    def get_guess(self):
        '''return if the position is guessed'''
        return self._guessed

    def __str__(self):
        return str(self._pos) + ' : ' + str(self._ship) + ' : ' + str(self._guessed)

class Board:
    '''
    An instance of this class describes a board  with a placement of ships.

    Attributes: self._poss： a 10 × 10 grid of positions, where each
                             position is a GridPos object.

                self._ships： a collection (list) of Ship objects.

    '''
    def __init__(self):
        self._poss = []
        for x in range(10):
            self._poss.append([GridPos(x,y) for y in range(10)])
        self._ships = []

    def guess(self, x, y):
        '''when the gridpos is guessed, determine which message should be printed

        Paramters: x, y： the coordinates of the position.
        '''
        pos = self._poss[x][y]  #get position.
           
        if pos._ship == None:
            if not pos._guessed:
                print("miss")
                pos._guessed = True
            else:
                print("miss (again)")
                
        #if ship is not empty.
        else:
            ship = pos._ship
            if not pos._guessed:
                if ship._num != 1:
                    print("hit")
                    ship._num -= 1
                else:
                    ship._num -= 1 
                    ship = ship._kind
                    print("{} sunk".format(ship))
                    self._ships.remove(ship)
                pos._guessed = True                   
            else:
                print("hit (again)")
        if len(self._ships) == 0:
            print("all ships sunk: game over")
            exit(1)
            
    def get_positions(self):
        '''return the postions'''
        return self._poss

    def get_ship(self):
        '''return the collection of ship objects'''
        return self._ships

    def __str__(self):
        return self._poss

class Ship:
    '''An instance of this class represents a ship .

    Attributes: self._kind: the kind of ship.

                self._size: the size of the ship.

                self._pos: the grid positions occupied by the ship.

                self._number: the number of grid positions occupied by
                                the ship that have not yet been hit.'''
    def __init__(self, line):
        elem = line.strip().split()
        self._kind = elem[0]
        size_dict = {"A":5 , "B":4, "S":3, "D":3, "P":2}
        self._size = size_dict[self._kind]
        
        
        x1 = int(elem[1])
        y1 = int(elem[2])
        x2 = int(elem[3])
        y2 = int(elem[4])

        try:
            assert x1 == x2 or y1 == y2
        except AssertionError:
            print("ERROR: ship not horizontal or vertical: " + line)
            sys.exit(1)

        try:
            assert max(x1,x2,y1,y2) <= 9 and min(x1,x2,y1,y2) >= 0    
        except AssertionError:
            print("ERROR: ship out-of-bounds: " + line)
            sys.exit(1)

        #if x1 equal to x2, set position to x1,y.
        if x1 == x2:
            self._pos = [(x1, y) for y in range(min(y1, y2), max(y1, y2)+1)]

        #else x1 nto equal to x2, set position to x,y1.
        else:
            self._pos = [(x, y1) for x in range(min(x1, x2), max(x1, x2)+1)]
            

        try:
            assert len(self._pos) == self._size
        except AssertionError:
            print("ERROR: incorrect ship size: " + line)
            sys.exit(1)
     
        self._num = self._size
        
    def get_kind(self):
        ''' return the kind of the ship'''
        return self._kind

    def get_size(self):
        ''' return the size of the ship'''
        return self._size

    def get_position(self):
        ''' return the position list of the ship'''
        return self._pos

    def get_number(self):
        ''' return the remaining number of the ship'''
        return self._num     

    def __str__(self):
        return str(self._kind) + ' : ' + str(self._size) + ' : ' + str(self._pos)
        

def main():
    board = player_1()
    player_2(board)

def player_1():
    '''
    This function is the player1's turn. Read in the contents of the placement
    file and initialize the board accordingly. Add the ship info into the board,
    then return the board object.

    Parameter: None
    
    Returns: board: the Board object with the Ship infomrmation.

    Pre-condition: board object do not exist.

    Post-condition: the ship has been added to the board object.
    '''
    
    filename = input()

    #try if file do not exist.
    try:
        file = open(filename)
    except FileNotFoundError:
        print("ERROR: Could not open file: " + filename)
        sys.exit(1)

    lines = file.readlines()

    board = Board()
    for line in lines:
        ship = Ship(line)

        try:
            for pos in ship._pos:
                assert board._poss[pos[0]][pos[1]]._ship == None
        except AssertionError:
            print("ERROR: overlapping ship: " + line)
            sys.exit(1)
            
        board._ships.append(ship._kind)
        
        for pos in ship._pos:
            board._poss[pos[0]][pos[1]]._ship = ship
            
    try:
        
        assert sorted(board._ships) == ['A', 'B', 'D', 'P', 'S']
    except AssertionError:
        print("ERROR: fleet composition incorrect")
        exit(1)
            
    file.close()
    return board

def player_2(board):
    '''
    This function is the player2's turn. Read in the contents for each guess,
    respond based on the effects of the guess.
    
    Parameter: board: the Board object created in 'player_1' function.

    Return: None

    Pre-condition: board object got from player_1 function.

    Post-condition: the respones from guess printed and the ship has been determined.

    
    '''
    filename = input()

    #try if file do not exist.
    try:
        file = open(filename)
    except FileNotFoundError:
        print("ERROR: Could not open file: " + filename)
        sys.exit(1)

    lines = file.readlines()
    for line in lines:
        
        line = line.strip()

        #get x,y from line.
        if line != "":
            x = int(line.split()[0])
            y = int(line.split()[1])

            #try if x,y both smaller than 10.
            try:
                assert x < 10 and y < 10
            except AssertionError:
                print("illegal guess")
                
                continue
            board.guess(x,y)
            
main()
