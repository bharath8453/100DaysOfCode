from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # Step 1: Build adjacency list and in-degree array
        adj = [[] for i in range(numCourses)]   # adjacency list
        indegree = [0] * numCourses             # indegree[i] = number of prerequisites for course i
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)          # prereq -> course
            indegree[course] += 1               # course has one more prerequisite

        # Step 2: Initialize queue with courses having no prerequisites (indegree = 0)
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken_courses = 0

        # Step 3: Process courses in BFS order
        while queue:
            current = queue.popleft()
            taken_courses += 1   # we "take" this course
            
            for neighbor in adj[current]:
                indegree[neighbor] -= 1         # remove dependency
                if indegree[neighbor] == 0:     # if no prereqs left
                    queue.append(neighbor)

        # Step 4: Check if we could take all courses
        return taken_courses == numCourses

sol = Solution()
print(sol.canFinish(2, [[1,0]]))      
print(sol.canFinish(2, [[1,0],[0,1]])) 