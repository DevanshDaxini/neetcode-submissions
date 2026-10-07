class Solution:
    def decodeString(self, s: str) -> str:
        
        #use a stack for this
        #hash map? not sure for what tho, maybe not even needed

        #idea is that you have letters in brackets and outside brackets there is a number. number is how many times you repeat that phrase in the brackets

        #have a hashmap that checks for the endings [ ]

        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        
        return "".join(stack)