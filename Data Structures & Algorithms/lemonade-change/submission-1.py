class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        change = Counter()

        for bill in bills:

            change[bill] += 1

            if bill == 10:

                if change[5]:

                    change[5] -= 1
                
                else:

                    return False

            elif bill == 20:

                if change[5] and change[10]:

                    change[5] -= 1
                    change[10] -= 1

                elif change[5] >= 3:

                    change[5] -= 3
                    
                else:

                    return False
        
        return True