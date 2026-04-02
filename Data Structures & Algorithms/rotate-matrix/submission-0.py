class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # transpose
        for r in range(n):
            for c in range(r):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp

        # reverse
        for r in range(n):
            matrix[r] = matrix[r][::-1]

