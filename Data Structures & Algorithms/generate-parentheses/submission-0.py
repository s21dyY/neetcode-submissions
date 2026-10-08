class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        out = []
        def bt(path, score):
            if len(path) >n*2:
                return
            
            if score == 0 and len(path) == n*2:
                out.append("".join(path))
                return
            
            for p in "()":
                path.append(p)
                if p == "(":
                    bt(path, score+1)
                elif score > 0 and  p == ")":
                    bt(path, score-1)
                
                path.pop()

        bt([], 0)

        return out

