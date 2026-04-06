class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        num_black = 0

        for i in range(k):

            if blocks[i] == "B":

                num_black += 1

        min_required_ops = k - num_black

        for i in range(k, len(blocks), 1):

            if blocks[i - k] == "B":

                num_black -= 1

            if blocks[i] == "B":

                num_black += 1

            min_required_ops = min(min_required_ops, k - num_black)

        return min_required_ops