class Solution:
    def longestPalindrome(self, s: str) -> str:
        t='^#'+'#'.join(s)+"#@"
        r,c=0,0
        p=[0]*len(t)
        for i in range(1,len(t)-1):
            mirror=2*c-i
            if i<r:
                p[i]=min(r-i,p[mirror])
            while t[i+p[i]+1]==t[i-p[i]-1]:
                p[i]+=1
            if i+p[i]>r:
                c,r=i,i+p[i]
        max_len,center=max((n,i) for i,n in enumerate(p))
        start=(center-max_len)//2
        return s[start:start+max_len]


'''SOLVED BY ADIT MUGDHA DAS'''