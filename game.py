import pygame
from random import randint
import sys

class Game:
    #defining colors (RGB format) used in game and frames per sec
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)
    BLUE = (0, 0, 255)
    FPS = 20

    #constructor for initializing variables and modules
    def __init__(self):
        pygame.init() #initialize pygame modules
        self.SCREEN_WIDTH = self.SCREEN_HEIGHT = 600 #size of square window

        self.BOX_SIZE = self.SCREEN_HEIGHT // 3 #width and height of each square in grid

        #Creating 3 by 3 board as 2d matrix
        #0 means space is empty
        #1 means player chose that space
        #2 means computer chose that space
        self.board = [[0,0,0], [0,0,0], [0,0,0]]

        #creating window and setting title
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("TicTacToe Game")


    #function to draw the lines on board
    def drawBoard(self):        
        #drawing horizontal lines
        for lineNum in range(1, 3):
            pygame.draw.line(self.screen, self.BLACK, (0, self.BOX_SIZE * lineNum), (self.SCREEN_WIDTH, self.BOX_SIZE * lineNum))

        #drawing vertical lines
        for lineNum in range(1, 3):
            pygame.draw.line(self.screen, self.BLACK,  (self.BOX_SIZE * lineNum, 0), (self.BOX_SIZE * lineNum, self.SCREEN_HEIGHT))

        pygame.display.update()


    #drawing X's onto screen (by player) given row and column number
    def drawX(self, rowIndex, colIndex):
        pygame.draw.line(self.screen, self.BLACK, (colIndex * self.BOX_SIZE, rowIndex * self.BOX_SIZE), ((colIndex + 1) * self.BOX_SIZE, (rowIndex + 1) * self.BOX_SIZE))
        pygame.draw.line(self.screen, self.BLACK, ((colIndex + 1) * self.BOX_SIZE, rowIndex * self.BOX_SIZE), (colIndex * self.BOX_SIZE, (rowIndex + 1) * self.BOX_SIZE))
        pygame.display.update()

    #drawing 'O' onto screen (random choice by computer)
    def drawO(self,rowIndex, colIndex):
        center_x = colIndex * self.BOX_SIZE + (0.5 * self.BOX_SIZE)
        center_y = rowIndex * self.BOX_SIZE + (0.5 * self.BOX_SIZE)
        center_of_circle = (center_x, center_y)
        pygame.draw.circle(self.screen, self.BLUE, center_of_circle, radius = 0.5 * self.BOX_SIZE - 5, width = 1)
        pygame.display.update()


    #Returns the row and column index of mouse click (x and y coordinates)
    #return -1 for row or/and column index if click position is unclear or outside the board
    def getRowColIndex(self, mouse_pos):
        #calculating row index first
        if mouse_pos[1] > 0 and mouse_pos[1] < self.BOX_SIZE:
            rowIndex = 0
        elif mouse_pos[1] > self.BOX_SIZE and mouse_pos[1] < 2 * self.BOX_SIZE:
            rowIndex = 1
        elif mouse_pos[1] > 2 * self.BOX_SIZE and mouse_pos[1] < 3 * self.BOX_SIZE:
            rowIndex = 2
        else:
            rowIndex = -1 
        
        #now calculating column index
        if mouse_pos[0] > 0 and mouse_pos[0] < self.BOX_SIZE:
            colIndex = 0
        elif mouse_pos[0] > self.BOX_SIZE and mouse_pos[0] < 2 * self.BOX_SIZE:
            colIndex = 1
        elif mouse_pos[0] > 2 * self.BOX_SIZE and mouse_pos[0] < 3 * self.BOX_SIZE:
            colIndex = 2
        else:
            colIndex = -1 
        
        return (rowIndex, colIndex)


    #Execute this when its the player's turn
    def playerTurn(self, rowIndex, colIndex):
        self.drawX(rowIndex, colIndex) #draw "X" where player clicked
        self.board[rowIndex][colIndex] = 1 #update board so that cell is now occupied by player
        pygame.time.wait(200) #wait 0.2 seconds
        

    #Execute this to handle computer's turn
    def computerTurn(self):
        #computer chooses random row and column
        rowIndex = randint(0,2) 
        colIndex = randint(0,2)

        #as long as chosen cell is occupied
        while self.board[rowIndex][colIndex] != 0: 
            #computer should choose again
            rowIndex = randint(0,2) 
            colIndex = randint(0,2)

        self.drawO(rowIndex, colIndex) #draw 'O'
        self.board[rowIndex][colIndex] = 2 #update board so that cell is occupied by computer


    #check to see if player or computer won by row
    #Return "p" if player won and return "c" if the computer won
    def checkRowWin(self):
        for row in range(0,3):
            if self.board[row][0] == self.board[row][1] and self.board[row][1] == self.board[row][2]: #if all numbers in row are same
                if self.board[row][0] == 1:
                    return "p"
                elif self.board[row][0] == 2:
                    return "c"

    #check to see if player or computer won by column
    #Return "p" if player won and return "c" if the computer won
    def checkColWin(self):
        for col in range(0,3):
            if self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col]: #if all numbers in col are same
                if self.board[0][col] == 1:
                    return "p"
                elif self.board[0][col] == 2:
                    return "c"

    #check to see if player or computer won by diagonal
    #Return "p" if player won and return "c" if the computer won
    def checkDiagonalWin(self):
        #check for winner in top-left to bottom-right diagonal
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]: #if all numbers in diagonal are same
            if self.board[0][0] == 1:
                return "p"
            elif self.board[0][0] == 2:
                return "c" 
            
        #check for winner in top-right to bottom-left diagonal
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            if self.board[0][2] == 1:
                return "p"
            elif self.board[0][2] == 2:
                return "c"

    #check to see if player won   
    def hasPlayerWon(self):
        # rowIndex = self.checkRowWin()
        # colIndex = self.checkColWin()
        # diagonalWin =  self.checkDiagonalWin()
        # print(rowIndex, colIndex, diagonalWin)
        if self.checkRowWin() == "p" or self.checkColWin() == "p" or self.checkDiagonalWin() == "p":
            return True 

    #check to see if computer won
    def hasComputerWon(self):
        if self.checkRowWin() == "c" or self.checkColWin() == "c" or self.checkDiagonalWin() == "c":
            return True

    #check to see if it is a tie (all spaces in board filled and no winner)
    def isItATie(self):
        #loop through every cell in the board
        for row in range(0, 3):
            for col in range(0,3):
                if self.board[row][col] == 0: #there is empty space so board not filled
                    return False 
        return True

    #display winning (or tie) screen depending on who won 
    def displayWinningScreen(self):
        winning_font = pygame.font.SysFont('arial', 20)

        if self.hasComputerWon():
            winning_surf = winning_font.render("You lost! Click anywhere on screen to play again", True, self.WHITE)
        elif self.hasPlayerWon():
            winning_surf = winning_font.render("You won! Click anywhere to play again", True, self.WHITE)
        else:
            winning_surf = winning_font.render("It was a TIE! Click anywhere to play again", True, self.WHITE)

        self.screen.fill(self.BLACK)
        self.screen.blit(winning_surf, (180, 200))
        pygame.display.update()

        #check to see if user wants to play again
        displayScreen = True
        while displayScreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #reset game by emptying out board variable and clearing screen
                    displayScreen = False
                    for row in range(0,3):
                        for col in range(0,3):
                            self.board[row][col] = 0

                    self.screen.fill(self.WHITE) #reset screen colour to white
                    self.drawBoard() #draw the lines on the board


    #main function which has game loop
    def main(self):
        clock = pygame.time.Clock()
        self.screen.fill(self.WHITE) #fill screen with white color
        self.drawBoard() #draw the lines on the board
        
        running = True
        while running:
            clock.tick(self.FPS) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #if you click "X" button
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN: #if player clicked the mouse
                    clickedPosition = event.pos
                    rowIndex, colIndex = self.getRowColIndex(clickedPosition)
                    
                    #if player made valid choice and the cell chosen was empty
                    if rowIndex != -1 and colIndex != -1 and self.board[rowIndex][colIndex] == 0: 
                        self.playerTurn(rowIndex, colIndex)
                        if self.hasPlayerWon():
                            self.displayWinningScreen()
                            #print("Player has won!")
                           

                        if self.isItATie():
                            self.displayWinningScreen()
                            #print("It is a TIE!!")
                           

                        self.computerTurn()
                        if self.hasComputerWon():
                            self.displayWinningScreen()
                            #print("Computer has won!")
                            
            pygame.display.update()

    

if __name__  == "__main__":
    g = Game()
    g.main()


    



