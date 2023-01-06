# !/usr/bin/env python
# -*- coding : utf-8 -*-
import pygame

width = height= 620
pygame.init()
screen = pygame.display.set_mode((width, height))
green = (0, 255, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
delay = 50
myfont = pygame.font.SysFont('monospace', width//10)


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
        self.current_turn = 'croix'
        self.finished = False

width_lines = 10
rects = []
width_rect = (width - 2 * width_lines)//3
offset  = width_rect//2

lines = [
        pygame.Rect(0, width_rect, width, width_lines),
        pygame.Rect(0, 2*width_rect + width_lines, width, width_lines),
        pygame.Rect(width_rect, 0, width_lines, height),
        pygame.Rect(2*width_rect + width_lines, 0, width_lines, height)
]

for j in range(3):
    for i in range(3):
        rects.append(pygame.Rect(i * (width_rect + width_lines), 
                                j * (width_rect + width_lines),
                                (width- 2*width_lines)//3,
                                (height - 2*width_lines)//3)
                                )
#print('rect', rects)

centers = []
for j in range(3):
    for i in range(3):
        centers.append(((i * (width_rect + width_lines) + offset), j * (width_rect + width_lines) + offset))
#print('centers', centers)


partie = Tictactoe()
running = True

while running:
    for event in pygame.event.get():
        (x, y) = pygame.mouse.get_pos()
        mouse_collider = pygame.Rect(x, y, 10, 10)

        if mouse_collider.collidelist(rects) != -1 and event.type == pygame.MOUSEBUTTONDOWN:
            print(mouse_collider.collidelist(rects))
            partie.joue(partie.tour_de(), mouse_collider.collidelist(rects)+1)
            #partie.to_str()
            partie.is_finished()
        if event.type == pygame.QUIT:
            running = False


    screen.fill(black)
    key = pygame.key.get_pressed()

    if key[pygame.K_ESCAPE]:
        end = True
    
    for i in range(4):
        pygame.draw.rect(screen, green, lines[i])

    for i in range(9):
        pygame.draw.rect(screen, (255, 0, 20*i), rects[i])
    
    for i in range(len(centers)):
        partie.grid[i]
        symbol_txt = myfont.render(partie.grid[i], False, green)
        screen.blit(symbol_txt, (
                            centers[i][0]-(symbol_txt.get_width()//2),
                            centers[i][1]-(symbol_txt.get_height()//2))
                            )


    pygame.time.delay(delay)
    pygame.display.update()

    if partie.finished == True:
        game_over_txt = myfont.render("GAME OVER", False, green)
        replay_txt = myfont.render("Press 'R' to Retry", False, green)
        screen.blit(game_over_txt,
                    (width//2-game_over_txt.get_width()//2,
                     height//2-game_over_txt.get_height()*4)
                    )
        screen.blit(replay_txt,
                    (width//2-replay_txt.get_width()//2,
                     height//2-replay_txt.get_height())
                    )
        print('finished')
        if key[pygame.K_r]:
            partie.reset()


pygame.quit()



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
