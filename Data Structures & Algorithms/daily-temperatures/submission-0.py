class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        '''

        initial ideas:

        Ok so based on the hint this is a stack question, so what we could do
        is something like, ok first number goes in, we see a hotter number,
        push the length to an array. Reset stack and then process the hotter number, processs until the end and if theres a hotter if not then push 0, rinse and repeat. but this becomes super slow? Not sure 



        stack = []
        result

        what if we had a way to keep track of the first number we're comparing to?


        



        push 30
        see 38
        is 38 larger then var? 
        push 1 to result



        input = [30,38,30,36,35,40,28]

        '''

        stack = []
        result = [0] * len(temperatures)


        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev

            stack.append(i)

            

        return result






        