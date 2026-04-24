from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # store word at end node


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Step 1: Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word   # mark complete word
        
        m, n = len(board), len(board[0])
        result = []

        # Step 2: DFS
        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            
            next_node = node.children[ch]
            
            # Found a word
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None   # avoid duplicates
            
            # Mark visited
            board[r][c] = '#'
            
            # Explore neighbors
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)
            
            # Restore cell
            board[r][c] = ch
            
            # Optimization: remove leaf node
            if not next_node.children:
                node.children.pop(ch)

        # Step 3: Start DFS from each cell
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        
        return result