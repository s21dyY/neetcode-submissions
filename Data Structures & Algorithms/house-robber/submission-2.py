class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        dp[2] = dp[0]+nums[2]
        
        #[2, 9, 10, 12, 16]
        for i in range(3, len(nums)):
            dp[i] = nums[i] + max(dp[0:i-1])
        
        print(dp)
        return max(dp[-1], dp[-2])
        