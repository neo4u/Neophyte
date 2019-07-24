import collections

class Solution:
    def findOrder(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # construct graph
        graph = {i: set() for i in range(n)}
        in_degrees = {i: 0 for i in range(n)}

        for course, prereq in edges:
            graph[prereq].add(course)
            in_degrees[course] += 1

        # init var
        q = collections.deque()
        visited = []

        # find nodes whose in degree == 0
        for index, in_degree in in_degrees.items():
            if in_degree == 0: q.append(index)

        # loop all nodes whose in degree == 0
        while q:
            index = q.popleft()
            visited.append(index)
            for g in graph[index]:
                in_degrees[g] -= 1
                if in_degrees[g] == 0:
                    q.append(g)

        return visited[::-1] if len(visited) == n else []

# The code is almost the same as "course schedule". The only difference is we keep the courses taken instead of remove them, everything else is the same.


# DFS
def canFinish(self, numCourses, prerequisites):
    graph = [[] for _ in xrange(numCourses)]
    visit = [0 for _ in xrange(numCourses)]
    for x, y in prerequisites:
        graph[x].append(y)
    def dfs(i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        return True
    for i in xrange(numCourses):
        if not dfs(i):
            return False
    return True
# if node v has not been visited, then mark it as 0.
# if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
# if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.

# BFS: from the end to the front
def canFinish1(self, numCourses, prerequisites):
    forward = {i: set() for i in xrange(numCourses)}
    backward = collections.defaultdict(set)
    for i, j in prerequisites:
        forward[i].add(j)
        backward[j].add(i)
    queue = collections.deque([node for node in forward if len(forward[node]) == 0])
    while queue:
        node = queue.popleft()
        for neigh in backward[node]:
            forward[neigh].remove(node)
            if len(forward[neigh]) == 0:
                queue.append(neigh)
        forward.pop(node)
    return not forward  # if there is cycle, forward won't be None

# BFS: from the front to the end    
def canFinish2(self, numCourses, prerequisites):
    forward = {i: set() for i in xrange(numCourses)}
    backward = collections.defaultdict(set)
    for i, j in prerequisites:
        forward[i].add(j)
        backward[j].add(i)
    queue = collections.deque([node for node in xrange(numCourses) if not backward[node]])
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        for neigh in forward[node]:
            backward[neigh].remove(node)
            if not backward[neigh]:
                queue.append(neigh)
    return count == numCourses
    
# DFS: from the end to the front
def canFinish3(self, numCourses, prerequisites):
    forward = {i: set() for i in xrange(numCourses)}
    backward = collections.defaultdict(set)
    for i, j in prerequisites:
        forward[i].add(j)
        backward[j].add(i)
    stack = [node for node in forward if len(forward[node]) == 0]
    while stack:
        node = stack.pop()
        for neigh in backward[node]:
            forward[neigh].remove(node)
            if len(forward[neigh]) == 0:
                stack.append(neigh)
        forward.pop(node)
    return not forward
        
# DFS: from the front to the end    
def canFinish(self, numCourses, prerequisites):
    forward = {i: set() for i in xrange(numCourses)}
    backward = collections.defaultdict(set)
    for i, j in prerequisites:
        forward[i].add(j)
        backward[j].add(i)
    stack = [node for node in xrange(numCourses) if not backward[node]]
    while stack:
        node = stack.pop()
        for neigh in forward[node]:
            backward[neigh].remove(node)
            if not backward[neigh]:
                stack.append(neigh)
        backward.pop(node)
    return not backward


import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # construct graph
        graph = collections.defaultdict(set)
        in_degrees = collections.defaultdict(int)

        for course, prereq in prerequisites:
            graph[prereq].add(course)
            in_degrees[course] += 1

        q, visited = [], []

        for node in range(numCourses):
            if in_degrees[node] != 0: continue
            q.append(node)
            visited.append(node)

        while q:
            node = q.pop(0)

            for nbr in graph[node]:
                if nbr in visited: continue
                in_degrees[nbr] -= 1
                if in_degrees[nbr] == 0:
                    q.append(nbr)
                    visited.append(nbr)

        return visited if len(visited) == numCourses else []

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        degree = [0]*numCourses
        for u,v in prerequisites:
            graph[v].append(u)
            degree[u]+= 1
            
        res = []
        queue = []
        for v in range(numCourses):
            if degree[v]==0:
                queue.append(v)

        n = numCourses
        while len(queue):
            front = queue.pop(0)
            res.append(front)
            n -= 1
            for neighbour in graph[front]:
                degree[neighbour] -= 1
                if degree[neighbour] == 0:
                    queue.append(neighbour)

        return res if n == 0 else []
