class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])

        def dfs(r, c):
            
            if r<0 or r >=rows or c<0 or c>=cols:
                return False
            if matrix[r][c]== target:
                return True
            #print(f"r:{r}, c:{c}, n:{ matrix[r][c] }")
            if matrix[r][c] > target:
                return dfs(r, c-1)
            else:
                return dfs(r+1, c)
        
        return dfs(0, cols-1)


        

        