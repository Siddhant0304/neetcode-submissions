class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]
        map = {}
        res = []

        for word in strs:
            key = tuple(sorted(word))
            if key in map:
                map[key].append(word)
            else:
                map[key] = [word]

        
        for v in map.values():
            res.append(v)
        
        print(map)
        return res

        

        