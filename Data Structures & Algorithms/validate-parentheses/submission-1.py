class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"}":"{", "]":"[", ")":"("}
        
        for c in s:
            if c in mapping.keys():
                if not stack or stack[-1] != mapping[c]:
                    return False
                stack.pop()
            else:
                stack += [c]
        
        if stack:
            return False
        return True
