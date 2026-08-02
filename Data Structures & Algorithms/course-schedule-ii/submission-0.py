class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prereq = {c:[] for c in range(numCourses)}
        for c, p in prerequisites:
            prereq[c].append(p)
        output = []
        visit = set()
        cycle = set()

        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            cycle.add(c)

            for pre in prereq[c]:
                if dfs(pre) == False:
                    return False
            cycle.remove(c)
            visit.add(c)
            output.append(c)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output



            
        
