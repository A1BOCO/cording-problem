class Solution:
    def findOrder(self, numCourses, prerequisites) -> List[int]:

        adj = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegrees[prerequisite[0]] += 1

        start = []

        for idx, indegree in enumerate(indegrees):
            if indegree == 0:
                start.append(idx)

        def dfs(pos, tmp_indegrees):

            ans.append(pos)
            for next_pos in adj[pos]:

                indegrees[next_pos] -= 1
                if indegrees[next_pos] == 0:
                    dfs(next_pos, tmp_indegrees)

        ans = []
        for course in start:

            dfs(course, indegrees.copy())
            if len(ans) == numCourses:
                return ans
        return []
