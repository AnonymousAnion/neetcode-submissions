class Solution:
    def majorityElement(self, nums: List[int], n = 3) -> List[int]:
        
        # Only at most 2 numbers can be more than 1/3 of
        # elements in nums. To find the numbers occurring more than 1/4
        # of the time, you'd track at most 3. Where n is the numbers occurring
        # more than 1/n of the time, we track at most n-1 frequences
        # and we check that they each occur more than 1//n times in nums.

        freqs = defaultdict(int)

        for num in nums:

            freqs[num] += 1

            if len(freqs) > n - 1:

                new_freqs = defaultdict(int)

                for val, c in freqs.items():

                    if c > 1:

                        new_freqs[val] = freqs[val] - 1

                freqs = new_freqs
        
        frequent_elements = []

        for key in freqs:

            if nums.count(key) > len(nums) // n:
                
                frequent_elements.append(key)

        return frequent_elements
                    