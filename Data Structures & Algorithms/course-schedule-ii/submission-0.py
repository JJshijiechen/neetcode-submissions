from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. 建图：pre -> crs（修完先修课 pre 才能解锁 crs）
        adj = [[] for _ in range(numCourses)]
        # 入度数组：记录每门课还剩几门先修课没修
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        # 2. 初始化队列：把所有“不需要任何先修课”（入度为 0）的课程入队
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        output = []

        # 3. BFS 模拟修课与解锁过程
        while q:
            node = q.popleft()
            output.append(node)  # 修完当前课程

            # 遍历依赖当前课程的后续课
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:  # 所有先修课都已修完，解锁
                    q.append(nei)

        # 4. 环检测：修完的课程总数等于 numCourses 则成功，否则说明有环
        return output if len(output) == numCourses else []