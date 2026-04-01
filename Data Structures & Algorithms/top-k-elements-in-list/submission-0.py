class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqs = Counter(nums)
        buckets: Dict = dict()

        for num in freqs:

            freq = freqs[num]

            if freq in buckets:

                buckets[freq].append(num)
            
            else:

                buckets.update({freq: [num]})

        # print("Buckets: ")
        # print(buckets)

        count = 0
        top_k_elements = []
        count_reached = False

        for i in range(len(nums), -1, -1):

            if count_reached:

                break

            possible_freq = i

            if possible_freq in buckets:

                #print("Matching top frequency: ", possible_freq)

                top_buckets = buckets[possible_freq]

                # print("Top Buckets: ")
                # print(top_buckets)

                for el in top_buckets:

                    #print("Adding Element: ", el)

                    top_k_elements.append(el)
                    count += 1

                    if count >= k:

                        count_reached = True
                        break;

        return top_k_elements