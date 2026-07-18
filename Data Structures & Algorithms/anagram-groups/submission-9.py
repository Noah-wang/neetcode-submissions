class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prev = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in prev:
                prev[key] = []
            prev[key].append( word)

        return list(prev.values())