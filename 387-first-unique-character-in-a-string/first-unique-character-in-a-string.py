class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for i, ch in enumerate(s):
            if ch not in hash_map:
                hash_map[ch] = [1, i]
            else:
                hash_map[ch][0] += 1

        for count, idx in hash_map.values():
            if count == 1:
                return idx
        

        return -1
        