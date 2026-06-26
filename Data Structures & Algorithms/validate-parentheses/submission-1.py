class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        paranthesis = {'(':')', '{':'}', '[':']'}
        for i in s:
            if i in paranthesis.keys():
                check.append(i)
            else:
                if not check:
                    return False
                top = check.pop()
                if paranthesis[top] != i:
                    return False
        return len(check) == 0
 


