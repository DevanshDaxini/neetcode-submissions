import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        #have to use a stack for the arethemetic operations
        #check to see if you reached a operators
        #have a hashmap that checks to see if the element is is in it
        #set a switch to True if the input in the stack is in the opperand
        #when switch is true apply that opperand to the values in in the stack
        #store the value of the operation in sum_1

        my_stack = []

        opp = {
            '+': operator.add, 
            '-': operator.sub, 
            '*': operator.mul, 
            '/': operator.truediv
        }

        for val in tokens:
            if val in opp:
                b = my_stack.pop()
                a = my_stack.pop()
                sum1 = int(opp[val](a, b))
                my_stack.append(sum1)
            else:
                my_stack.append(int(val))
        
        return my_stack[0]