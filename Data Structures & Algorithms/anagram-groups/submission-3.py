class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap (key: sorted word, value: list of strings containing the letters in sorted word)
        anagram_map = {}

        # loop through each word
        for word in strs:
            # sort word
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagram_map:
                # create a new KV pair
                anagram_map[sorted_word] = []   
            # add word matched to the sorted word into map
            anagram_map[sorted_word].append(word)
        
        # return the sublists in a big list
        return list(anagram_map.values())