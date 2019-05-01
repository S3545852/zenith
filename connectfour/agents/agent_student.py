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
        
        for row in range(0, board.height):
            for col in range(0, board.width -2):
                if(board.get_cell_value(row, col) == p2 and board.get_cell_value(row, col + 1) == p2):
                    if(board.get_cell_value(row, col + 2) == p2):
                        playerTwoTotalThreeConsecutive += 1;
                    else:
                        playerTwoTotalTwoConsecutive += 1;
                

        for row in range(0, board.height):
            for col in range(0, board.width -2):
                if(board.get_cell_value(row, col) == p1 and board.get_cell_value(row, col + 1) == p1):
                    print(board.get_cell_value(row, col));
                    if(board.get_cell_value(row, col + 2) == p1):
                        playerOneTotalThreeConsecutive += 1;
                    else:
                        playerOneTotalTwoConsecutive += 1;
                            

        playerTwoScore = playerTwoTotalTwoConsecutive + playerTwoTotalThreeConsecutive * 1.75;
        playerOneScore = playerOneTotalTwoConsecutive + playerOneTotalThreeConsecutive * 1.75;

        print(playerOneTotalTwoConsecutive);
        print("two = ", playerTwoScore);
        print("one = ", playerOneScore);
        print();
                    
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
