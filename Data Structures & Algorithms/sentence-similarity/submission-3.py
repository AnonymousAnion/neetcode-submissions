class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        # Continue Here:
        # There may be multiple words similar to a word
        # so maintain sets of similar words at each mapping
        mappings: Dict[str, set] = dict()

        for pair in similarPairs:

            if pair[0] not in mappings:

                mappings.update({pair[0]: set(pair)})
            
            else:

                mappings[pair[0]].add(pair[1])

            if pair[1] not in mappings:

                mappings.update({pair[1]: set(pair)})

            else:

                mappings[pair[1]].add(pair[0])

        if len(sentence1) != len(sentence2):

            return False

        for i in range(len(sentence1)):

            if sentence1[i] != sentence2[i]:

                if sentence1[i] in mappings and sentence2[i] in mappings[sentence1[i]]:

                    continue

                elif sentence2[i] in mappings and sentence1[i] in mappings[sentence2[i]]:

                    continue

                else:

                    return False

        return True