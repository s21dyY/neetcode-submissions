class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        visited = set()
        def dfs(idx):
            if idx >= len(nums)-1:
                return True
            
            jump = nums[idx]
            if jump ==0:
                return False
            if idx in visited:
                return False
            visited.add(idx)
            
            return True in  [dfs(idx + i ) for i in range(1, jump+1)]

        return dfs(0)
            