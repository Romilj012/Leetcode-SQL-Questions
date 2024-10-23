class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != "]":
                stack.append(i) 
            else:
                a = ""
                while stack[-1] != "[":
                    a = stack.pop() + a
                stack.pop()
                k = ""    
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*a)
        return "".join(stack)



