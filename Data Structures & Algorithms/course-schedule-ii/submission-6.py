class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        out = []

        while q:
            
            node = q.popleft()
            out.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return out if len(out) == numCourses else []
