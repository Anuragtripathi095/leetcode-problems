class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=n*[False]
        def dfs(city):
            for nei in range(n):
                if isConnected[city][nei]==1 and not visited[nei]:
                    visited[nei]=True
                    dfs(nei)
        provinces=0
        for i in range(n):
            if not visited[i]:
                provinces+=1
                visited[i]=True
                dfs(i)
        return provinces

