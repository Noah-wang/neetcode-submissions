class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prevMap = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in prevMap:
                prevMap[key] = []

            prevMap[key].append(word)
        return list(prevMap.values())