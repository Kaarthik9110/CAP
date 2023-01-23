class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[]
        c=k=0
        for i in s:
            if i not in l:
                l.append(i)
                c=c+1
                k=max(k,len(l))
        else:
            c=0
            l=[]
        return k
