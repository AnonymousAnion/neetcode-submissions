import string
from typing import Dict, List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams: Dict[str, List[str]] = dict()
        
        for word in strs:

            # print("Current Word: ", word)

            # Form the key for the word
            letter_frequencies = []

            freqs = Counter(word)

            for char in string.ascii_lowercase:

                freq = freqs[char]
                letter_frequencies.append(str(freq) + ",")

            hash_key = "".join(letter_frequencies)

            # print("Hash Key: ", hash_key)

            if hash_key not in anagrams:

                anagrams.update({hash_key: [word]})

            else:

                anagrams[hash_key].append(word)

            # print("Anagrams: ")
            # print(anagrams)

        two_dimensional_list = []

        for key in anagrams:

            two_dimensional_list.append(anagrams[key])

        return two_dimensional_list


