class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[1])
        op, cl = intervals[0][0],intervals[0][1]

        count = 0
        for start, end in intervals[1:]:
            
            # if overlap
            if start < cl :
                count +=1
            elif end > cl:
                cl = end
   
        return count