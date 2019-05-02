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
        playerTwoTwo = 0;
        playerTwoThree = 0;
        
        playerOneTwo = 0;
        playerOneThree = 0;

        p2 = 2;
        p1 = 1;
        win = -1;


        p1RowScore = 0;
        p1Score = 0;
        p2RowScore = 0;
        p2Score = 0;

        for row in range(0, board.height):
            p1RowScore = checkRow(board, row, win, True);
            print("p1RowScore = ", p1RowScore)
            p1Score += p1RowScore * p1RowScore;
        for row in range(0, board.height):
            p2RowScore = checkRow(board, row, win, False);
            print("p2RowScore = ", p2RowScore)
            p2Score += p2RowScore * p2RowScore;

        print()
            

        if(p1Score == win and p2Score == win):
            print("Draw move")
            return 0.0;
        if(p1Score == win):
            print("p1 win")
            return 1;
        if(p2Score == win):
            print("p2 win")
            return -1;

        if(p1Score > p2Score):
            ret = normalize(p1Score, 0.0, p1Score) - normalize(p2Score, 0.0, p1Score)
            print("ret = ", ret)
            return ret
        else:
            if(p1Score == 0 and p2Score == 0):
                return 0;
            else:
                ret = normalize(p2Score, 0.0, p2Score) - normalize(p1Score, 0.0, p2Score)
                print("ret = ", ret)
            return ret
        
            
#           print(checkRow(board, row));
 #       print();



#        for row in range(0, board.height):
#            for col in range(0, board.width):
#                ret = getPiecesInWiningRow(board, row, col, True);                
#                if(ret != False):
#                    if(ret == 2):
#                        playerOneTwo += ret;
#                    else:
#                        playerOneThree += ret;
#                if(col >= board.width):
#                    break;
                    
#            	if(board.get_cell_value(row, col) == 2):
 #                   return 1.0;
                
        """
        Your evaluation function should look at the current state and return a score for it. 
        As an example, the random agent provided works as follows:
            If the opponent has won this game, return -1.
            If we have won the game, return 1.
            If neither of the players has won, return a random number.
        """

        """
        These are the variables and functions for board objects which may be helpful when creating your Agent.
        Look into board.py for more information/descriptions of each, or to look for any other definitions which may help you.

        Board Variables:
            board.width 
            board.height
            board.last_move
            board.num_to_connect
            board.winning_zones
            board.score_array 
            board.current_player_score

        Board Functions:
            get_cell_value(row, col)
            try_move(col)
            valid_move(row, col)
            valid_moves()
            terminal(self)
            legal_moves()
            next_state(turn)
            winner()
        """
        return 0.5;             # 
#        return random.uniform(0, 1)

#returns false if row not a winable row



def checkRow(board, row, p1Turn, win):
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
            print("currRow = ", currRow)
            return win;    # This is a wining move!
    score += currRow;

    print("score = ", score)
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




def normalize(x, min, max):
    return (x - min) / max - min

                        
def getPiecesInWiningRow(board, row, colOffset, p1Turn):
            p2 = 2;
            p1 = 1;
            rowLen = 4;
            rowScore = 0;

            print("colOffset = ", colOffset, "board.width = ", board.width);
            if(colOffset + rowLen > board.width):
                return False;

            if(p1Turn):
                for col in range(colOffset, colOffset + rowLen):
                    if(board.get_cell_value(row, col) == p2):
                        return False;
                    if(board.get_cell_value(row, col) == p1):
                        rowScore += 1;
            else:
                for col in range(colOffset, colOffset + rowLen):
                    if(board.get_cell_value(row, col) == p1):
                        return False;
                    if(board.get_cell_value(row, col) == p2):
                        rowScore += 1;

            print("rowScore = ", rowScore);
            return rowScore;
            
