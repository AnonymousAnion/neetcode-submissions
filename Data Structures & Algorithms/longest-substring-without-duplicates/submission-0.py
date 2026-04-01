class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        char_index_mappings: Dict[str, int] = dict()
        current_length = 0
        max_length = 0
        
        for r, char in enumerate(s):

            if char in char_index_mappings:

                new_l = char_index_mappings[char] + 1

                for l in range(l, new_l):

                    char_to_remove = s[l]

                    del char_index_mappings[char_to_remove]

                l = new_l
            
            char_index_mappings.update({char: r})
            current_length = (r - l) + 1
            max_length = max(max_length, current_length)

        return max_length
        