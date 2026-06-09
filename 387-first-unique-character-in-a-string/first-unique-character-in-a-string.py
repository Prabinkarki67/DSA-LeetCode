class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for i in s:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        for key, value in hash_map.items():
            if value == 1:
                return s.index(key)
        

        return -1
        