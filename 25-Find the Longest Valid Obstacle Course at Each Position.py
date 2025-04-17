class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        st=[]
        ans=[]
        for i in obstacles:
            idx=bisect_right(st,i)
            ans.append(idx+1)
            if idx==len(st):
                st.append(i)
            else:
                st[idx]=i
        return ans

'''SOLVED BY ADIT MUGDHA DAS'''