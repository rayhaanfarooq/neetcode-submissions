class Solution:
    def isValid(self, s: str) -> bool:

        '''

        So we have 2 different kinds of bracks 
        (
        [
        {

        So we can use 3 stacks one for each
        just append the {
        then when we get a } pop one from the stack. Then check
        if all 3 are empty

        We need a end condition, is it to check if the others are
        empty?

        One stack

        if its a closing, check if the other one is a opening

        Stack: [(


        '''
        stack = []

        closing = {")" : "(", "}" : "{", "]" : "["}
        


        for char in s:
            if char not in closing:
                stack.append(char)

            else:
                if stack and stack[-1] == closing[char]:
                    stack.pop()

                else:
                    return False

        return stack == []









        
        