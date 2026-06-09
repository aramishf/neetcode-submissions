class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        # two hashmap for strings
        # key (char), value (count)
        # s[r] = 2

        count_char_s = {}
        count_char_t = {}

        for i in range(len(s)):
            if s[i] in count_char_s:
                count_char_s[s[i]] += 1
            else:
                count_char_s[s[i]] = 1

        for i in range(len(t)):
            if t[i] in count_char_t:
                count_char_t[t[i]] += 1
            else:
                count_char_t[t[i]] = 1

        return count_char_s == count_char_t
