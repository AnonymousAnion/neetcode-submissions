class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        mappings = {value: index for index, value in enumerate(nums2)}
        index_mapping = []

        for num in nums1:

            # should be present from problem description, but just in case
            if num in mappings:

                index_mapping.append(mappings[num])

        return index_mapping