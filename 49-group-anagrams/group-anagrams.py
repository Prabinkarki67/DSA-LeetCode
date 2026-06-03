class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            hash_mp = {}
            for ch in strs:
                key = ''.join(sorted(ch))
                if key not in hash_mp:
                    hash_mp[key] = []
                hash_mp[key].append(ch)
            res = []
            for i in hash_mp:
                res.append(hash_mp[i])
            return res