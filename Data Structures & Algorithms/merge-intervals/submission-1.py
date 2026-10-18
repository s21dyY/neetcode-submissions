class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: (x[0],x[1]))
        res = [intervals[0]]
        for interval in intervals:            
            # merge
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])

            else:
                res.append(interval)
        
        return res

