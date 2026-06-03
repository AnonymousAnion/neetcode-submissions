class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        top_five = defaultdict(list)

        sorted_items = sorted(items, key=lambda x: x[1], reverse = True)
        
        for student, score in sorted_items:

            if len(top_five[student]) < 5:

                top_five[student].append(score)

        final_list = []

        for student_id, top_scores in top_five.items():

            final_list.append([student_id, sum(top_scores) // 5])

        final_list = sorted(final_list, key=lambda x: x[0])

        return final_list