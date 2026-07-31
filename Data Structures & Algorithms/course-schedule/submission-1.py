class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        visited = set()
        recStack = set()
        
        def dfs(node):
            if node in recStack:
                return False
            if node in visited:
                return True

            visited.add(node)
            recStack.add(node)

            for neighbor in graph[node]:
                if dfs(neighbor) == False:
                    return False
            recStack.remove(node)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True


                





        