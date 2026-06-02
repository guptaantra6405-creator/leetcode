class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = [] 
        n = len(temperatures)
        ans = [0]* n
        for i in range(n):
            while st and temperatures[i]>st[-1][0]:
                previdx = st[-1][1]
                numdays = i-previdx
                ans[previdx] = numdays
                st.pop()
            st.append((temperatures[i], i))
        return ans