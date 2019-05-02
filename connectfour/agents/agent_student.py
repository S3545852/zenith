from connectfour.agents.computer_player import RandomAgent
import random


class StudentAgent(RandomAgent):
    def __init__(self, name):
        super().__init__(name)
        self.MaxDepth = 1

    def get_move(self, board):
        """
        Args:
            board: An instance of `Board` that is the current state of the board.

        Returns:
            A tuple of two integers, (row, col)
        """

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            next_state = board.next_state(self.id, move[1])
            moves.append(move)
            vals.append(self.dfMiniMax(next_state, 1))

        bestMove = moves[vals.index(max(vals))]
        return bestMove

    def dfMiniMax(self, board, depth):
        # Goal return column with maximized scores of all possible next states

        if depth == self.MaxDepth:
            return self.evaluateBoardState(board)

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            if depth % 2 == 1:
                next_state = board.next_state(self.id % 2 + 1, move[1])
            else:
                next_state = board.next_state(self.id, move[1])

            moves.append(move)
            vals.append(self.dfMiniMax(next_state, depth + 1))

        if depth % 2 == 1:
            bestVal = min(vals)
        else:
            bestVal = max(vals)

        return bestVal

    
    def evaluateBoardState(self, board):
        #We store any the number of consecutive coloums found with a game piece for player one and two
        p2 = 2;
        p1 = 1;
        win = -1;
        p1RowScore = 0;
        p1Score = 0;
        p2RowScore = 0;
        p2Score = 0;

#        for row in range(0, board.height):
  #          p1RowScore = checkRow(board, row, win, True);
 #           p1Score += p1RowScore * p1RowScore;

#        for row in range(0, board.height):
          #p2RowScore = checkRow(board, row, win, False);
         # p2Score += p2RowScore * p2RowScore;

        #p1Score =  p1Score / 50;
        #p2Score = p2Score / 50;


        for col in range(0, board.width):
            p1ColScore = checkColumn(board, col, win, True);
            p1Score += p1ColScore * p1ColScore;
        for col in range(0, board.width):
            p1ColScore = checkColumn(board, col, win, False);
            p2Score += p2RowScore * p2RowScore;

#        print("p1Score = ", p1Score)
 #       print("p2Score = ", p2Score)

#        if(checkFor3P1(board, p1)):
 #           print("We have a bad move")
  #          p1Score = 0
   #         p2Score = 0
    #        for row in range(0, board.height):
     #           p1RowScore = checkRow(board, row, win, True);
      #          p1Score += p1RowScore * p1RowScore;
#
 #           for row in range(0, board.height):
  #              p2RowScore = checkRow(board, row, win, False);
   #             p2Score += p2RowScore * p2RowScore;
    #            
     #       ret = 0;
      #      if(p1Score > p2Score):
       #         ret = produce_range(p1Score)
        #    else:
         #       if(p2Score > p1Score):
          #          ret = -produce_range(p2Score)

#            return -1;           # This moves has three consecutive p1's and thus is bad for p2
        

        ret = 0;
          
        if(p1Score > p2Score):
            ret = produce_range(p1Score)
        else:
            if(p2Score > p1Score):
                ret = -produce_range(p2Score)


#        print("ret = ", ret)
 #       print()

        return ret;

    
def produce_range(score):
    if(score <= 1000):
        score /= 1000;
    return score;


def checkRow(board, row, win, p1Turn):
    score = 0;              # If currRow == winRowLen return -1, else return score
    winRowLen = 4;
    p1 = 1;
    p2 = 2;

    currRow = 0;
    for c in range(0, board.width - winRowLen + 1):
        if(p1Turn):
            currRow = checkRowInner(board, row, winRowLen, c, p1, p2)
        else:
            currRow = checkRowInner(board, row, winRowLen, c, p2, p1)
        if(currRow == winRowLen):
            return win;    # This is a wining move!
        score += currRow;
        
    return score;
	

def checkRowInner(board, row, winRowLen, c, p1, p2):
    currRow = 0;
    for col in range(c, c + winRowLen):
        if(board.get_cell_value(row, col) == p1):
            currRow += 1;
        else:
            if(board.get_cell_value(row, col) == p2):
                currRow = 0;
                break;
        
    return currRow;


def checkColumn(board, col, win, p1Turn):
    score = 0;
    winColLen = 4;
    p1 = 1;
    p2 = 2;

    currCol = 0;
    for r in range(0, board.height - winColLen + 1):
        if(p1Turn):
            currCol = checkColInner(board, col, winColLen, r, p1, p2)
        else:
            currCol = checkColInner(board, col, winColLen, r, p2, p1)
        if(currCol == winColLen):
            return win;
        score += currCol;

    return score;
    

def checkColInner(board, col, winColLen, r, p1, p2):
    currCol = 0;
    for row in range(r, r + winColLen):
        if(board.get_cell_value(row, col) == p1):
            currCol +=1;
        else:
            if(board.get_cell_value(row, col) == p2):
                currCol = 0;
                break;
    return currCol;


def checkFor3P1(board, p1):
    if(checkColumnsFor3P1(board, p1)):
        return True;
#    else:
 #       if(checkRowsFor3P1(board, p1)):
  #          return True;
   #     else:
    #        if(checkDiagonalLRFor3P1(board, p1)):
     #           return True;
      #      else:
       #         if(checkDiagonalRLFor3P1(board, p1)):
        #            return True;
    return False;


def checkColumnsFor3P1(board, p1):
    for row in range(0, board.height):
        for col in range(0, board.width -3):
            if(board.get_cell_value(row, col) == p1 and board.get_cell_value(row, col +1) == p1 and board.get_cell_value(row, col +2) == p1):
                return True;
    return False;
            
