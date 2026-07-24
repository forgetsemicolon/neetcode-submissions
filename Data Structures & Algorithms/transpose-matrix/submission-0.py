class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix[0]), len(matrix)

        res = [[0 for r in range(COLS)] for c in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                res[r][c] = matrix[c][r]


        return res