class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, columns, squares = defaultdict(int), defaultdict(int), defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue

                cur_row = f"row{(i+1)}_{board[i][j]}"
                cur_col = f"column{(j+1)}_{board[i][j]}"
                cur_sqr = f"sqr{int(i/3)}_{int(j/3)}_{board[i][j]}"

                rows[cur_row] += 1
                columns[cur_col] += 1
                squares[cur_sqr] += 1

        
        hashtables = [rows, columns, squares]
        if any(val > 1 for ht in hashtables for val in ht.values()):
            return False
        return True