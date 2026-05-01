class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]
        map = {}
        res = []

        for word in strs:
            key = tuple(sorted(word))
            if key not in map:
                map[key] = []
            map[key].append(word)
           
        
        # for v in map.values():
        #     res.append(v)
        # return res
        
        return list(map.values())

        

        