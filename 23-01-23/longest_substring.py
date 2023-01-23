class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[]
        res=-1
        if len(s)==0:
            return 0
        elif(len(s)==1):
            return 1
        else:
            for i in range(len(s)):
                if s[i] not in l:
                    l.append(s[i])
                else:
                    res=max(len(l),res)
                    ind=l.index(s[i])
                    l=l[ind+1:]
                    l.append(s[i])
        res=max(res,len(l))
        return res
