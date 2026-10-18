class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = set()
        def dfs(idx):
            if idx >= len(nums)-1:
                return True
            if idx in visited:
                return False
            
            visited.add(idx)
                        
            for i in range(1, nums[idx]+1):
                if dfs(idx + i):
                    return True
            return False
            
        return dfs(0)
            