class TicTacToe:
    
    # O(1) time O(n) space

    def __init__(self, n: int):
        
        self.rowsPlayer1 = [0] * n
        self.colsPlayer1 = [0] * n
        # row == col
        self.diagPlayer1 = 0
        # col == COLS - row - 1
        self.antiDiagPlayer1 = 0
        
        self.rowsPlayer2 = [0] * n
        self.colsPlayer2 = [0] * n
        # row == col
        self.diagPlayer2 = 0
        # col == COLS - row - 1
        self.antiDiagPlayer2 = 0
        
        self.n = n
        
        
        
        

    def move(self, row: int, col: int, player: int) -> int:
        
        if player == 1:
            self.rowsPlayer1[row]+=1
            self.colsPlayer1[col]+=1
            if row == col:
                self.diagPlayer1+=1
            if col == self.n - row - 1:
                self.antiDiagPlayer1+=1

            if self.rowsPlayer1[row] == self.n or self.colsPlayer1[col] == self.n or self.diagPlayer1 == self.n or self.antiDiagPlayer1 == self.n:
                return player
            return 0
        
        if player == 2:
            self.rowsPlayer2[row]+=1
            self.colsPlayer2[col]+=1
            if row == col:
                self.diagPlayer2+=1
            if col == self.n - row - 1:
                self.antiDiagPlayer2+=1

            if self.rowsPlayer2[row] == self.n or self.colsPlayer2[col] == self.n or self.diagPlayer2 == self.n or self.antiDiagPlayer2 == self.n:
                return player
            return 0
        
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
