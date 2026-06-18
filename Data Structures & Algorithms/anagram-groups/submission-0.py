class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_s = ''.join(sorted(word))
            anagram_map[sorted_s].append(word)

        return list(anagram_map.values())

        