class Solution:

    def encode(self, strs: List[str]) -> str:

        encodings = [str(len(word)) + "#" + word for word in strs]
        
        combined_encoding = "".join(encodings)

        print("Encoding: ", combined_encoding)

        return combined_encoding

    def decode(self, s: str) -> List[str]:

        words: List[str] = []
        index = 0

        while index < len(s):

            end_index = 0

            for i in range(index, len(s)):

                char = s[i]

                if "#" == char:

                    end_index = i
                    break

            print("[{0}:{1}]".format(index, end_index))

            # Grab the current word length
            word_length = int(s[index: end_index])
            print("Word Length: ", word_length)

            words.append(s[end_index + 1: end_index + 1 + word_length])

            index = end_index + word_length + 1

        print("Words: ")
        print(words)

        return words

