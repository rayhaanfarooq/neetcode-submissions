class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        #Setup adjacency list
        graph = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        #State + return
        state = [0] * numCourses
        result = []

        def dfs(course):
            if state[course] == 1:
                return False

            if state[course] == 2:
                return True
            
            state[course] = 1

            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False


            state[course] = 2
            result.append(course)
            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return result[::-1]
                

            
            