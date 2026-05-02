class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s))+'.')
            res.append(s)
        print(''.join(res))
        print(res)
        return ''.join(res)
        

    def decode(self, s: str) -> List[str]:
        res = []
        cntr = 0
        while cntr < len(s):
            j = cntr
            numl = []
            while s[j]!='.':
                numl.append(str(s[j]))
                j+=1
                cntr+=1 
            curlen = int(''.join(numl))
            ele = s[cntr+1:(curlen+cntr+1)]
            res.append(ele)
            cntr+=(curlen+1)
   
        return res
    
