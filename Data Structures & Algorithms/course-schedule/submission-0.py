class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereq_map = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:

            prereq_map[course].append(prereq)

        # DFS track, detect if visting node within track
        track = set()
        
        def dfs(course: int):

            if course in track:

                return False

            if not prereq_map[course]:

                return True

            track.add(course)

            for prereq in prereq_map[course]:

                if not dfs(prereq):

                    return False

            track.remove(course)
            prereq_map[course] = []

            return True
        
        for course in range(numCourses):

            if not dfs(course): return False

        return True