# !/usr/bin/env python
# -*- coding : utf-8 -*-



class Tictactoe():

    def __init__(self):
        self.grid = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.current_turn = 'croix'
        self.next_turn = 'rond'
        self.finished = False


    def tour_de(self):
        return self.current_turn

    def joue(self, player, pos):
        if self.finished == True:
            print('Partie finie vous ne pouvez pas jouer.')
            return
        else:
            if self.grid[pos - 1] != ' ':
                print('Veuillez jouer un emplacement inutilisé')
                return
            else:
                if player == 'croix':
                    self.grid[pos - 1] = 'X'
                else:
                    self.grid[pos - 1] = 'O'
            self.current_turn, self.next_turn = self.next_turn, self.current_turn

    def to_str(self):
        for i in range(0, 8, 3):
            print( " {} | {} | {} ". format(self.grid[i], self.grid[i+1], self.grid[i+2]))

    def is_finished(self):
        #did someone win ?
        winning_sign = None
        #raw
        for i in range(0,9,3):
            if self.grid[i] == self.grid[i+1] == self.grid[i+2] != ' ':
                winning_sign = self.grid[i]
                self.finished = True
        #column
        for i in range(0, 3):
            if self.grid[i] == self.grid[i+3] == self.grid[i+6] != ' ':
                winning_sign = self.grid[i]
                self.finished = True
        #left to right diag
        if self.grid[0] == self.grid[4] == self.grid[8] != ' ':
            winning_sign = self.grid[0]
            self.finished = True
        #right to left diag
        if self.grid[2] == self.grid[4] == self.grid[6] != ' ':
            winning_sign = self.grid[2]
            self.finished = True

        if winning_sign != None:
            if winning_sign == 'X':
                return 'croix'
            elif winning_sign == 'O':
                return 'rond'

        #are all pos filled ?
        if ' ' in self.grid:
            return False
        #see if game is null
        elif not ' ' in self.grid:
            self.finished = True
            return 'null'

    def reset(self):
        self.grid = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.current_turn = 'rond'



partie = Tictactoe()
partie.joue(partie.tour_de(), 1)
partie.joue(partie.tour_de(), 3)
partie.joue(partie.tour_de(), 2)
partie.joue(partie.tour_de(), 4)
partie.joue(partie.tour_de(), 5)
partie.joue(partie.tour_de(), 9)
partie.joue(partie.tour_de(), 7)
partie.joue(partie.tour_de(), 8)
partie.joue(partie.tour_de(), 6)
print(partie.is_finished())
partie.joue(partie.tour_de(), 6)
partie.to_str()
partie.reset()



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
