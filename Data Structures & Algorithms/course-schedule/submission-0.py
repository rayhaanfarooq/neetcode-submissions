class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        So this is a problem to detect cycles, I can use bfs or dfs to solve this
        How would I solve this? 0 idea 


        '''

        #We have a edges, and make the adjcanency list 
        
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        #Keep a state for each node that exists
        state = [0] * numCourses

        #Setup dfs for cycle detection, if we see 1 return false if 2 return true

        def dfs(course):

            #If we see the course again while its being explored, return false
            if state[course] == 1:
                return False

            #Optional memoization
            if state[course] == 2:
                return True

            #Make the course state, visiting
            state[course] = 1

            #explore all neighbours
            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False

            #Done exploring, make the state finished
            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
            

            























        