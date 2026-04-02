class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        i = 0

        while i < 9:
            row = set()
            for j in range(9):
                if board[i][j] in row and board[i][j] != ".":
                    print(board[i][j])
                    return False
                row.add(board[i][j])
            
            i += 1

        j = 0

        while j < 9:
            col = set()
            for i in range(9):
                if board[i][j] in col and board[i][j] != ".":
                    print(board[i][j])
                    return False
                col.add(board[i][j])
            
            j += 1

        for box in range(9):
            seen = set()

            for i in range(3):
                for j in range(3):
                    row = (box//3) * 3 + i
                    col = (box%3) * 3 + j
                    if board[row][col] in seen and board[row][col] != ".":
                        print(board[row][col])
                        return False
                    seen.add(board[row][col])

        [[".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]]

        # box = set()
        # for i in range(3):
        #     for j in range(3):
        #         if board[i][j] in box and board[i][j] != ".":
        #             return False
        #         box.add(board[i][j])

        # box = set()
        # for i in range(3):
        #     for j in range(3,6):
        #         if board[i][j] in box and board[i][j] != ".":
        #             return False
        #         box.add(board[i][j])

        # box = set()
        # for i in range(3):
        #     for j in range(6,9):
        #         if board[i][j] in box and board[i][j] != ".":
        #             return False
        #         box.add(board[i][j])

        # box = set()
        # for i in range(3,6):
        #     for j in range(3):
        #         if board[i][j] in box and board[i][j] != ".":
        #             return False
        #         box.add(board[i][j])

        # box = set()
        # for i in range(3,6):
        #     for j in range(3,6):
        #         if board[i][j] in box and board[i][j] != ".":
        #             return False
        #         box.add(board[i][j])

        # box = set()
        # for i in range(3,6):
        #     for j in range(6,9):
        #         if board[i][j] in box and board[i][j] != ".":
        #             return False
        #         box.add(board[i][j])

        # box = set()
        # for i in range(6,9):
        #     for j in range(3):
        #         if board[i][j] in box and board[i][j] != ".":
        #             return False
        #         box.add(board[i][j])


        # box = set()
        # for i in range(6,9):
        #     for j in range(3,6):
        #         if board[i][j] in box and board[i][j] != ".":
        #             return False
        #         box.add(board[i][j])

        # box = set()
        # for i in range(6,9):
        #     for j in range(6,9):
        #         if board[i][j] in box and board[i][j] != ".":
        #             return False
        #         box.add(board[i][j])
        

        return True