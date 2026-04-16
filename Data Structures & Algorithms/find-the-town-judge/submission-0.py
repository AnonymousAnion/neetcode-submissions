class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        #print(trust)

        trusting = dict()
        trusted = dict()
        people = set()

        for t in trust:

            people.add(t[0])
            people.add(t[1])

            if t[0] not in trusting:

                trusting.update({t[0]: [t[1]]})

            else:

                trusting[t[0]].append(t[1])

            if t[1] not in trusted:

                trusted.update({t[1]: [t[0]]})

            else:

                trusted[t[1]].append(t[0])

        # print("people: ", people)
        # print("trusting: ", trusting)
        # print("trusted: ", trusted)

        for t in trusted:

            if len(trusted[t]) == len(people) - 1 and t not in trusting:

                return t

        return -1