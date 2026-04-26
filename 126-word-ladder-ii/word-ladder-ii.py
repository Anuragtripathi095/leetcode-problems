from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # BFS
        parents = defaultdict(list)
        level = {beginWord}
        found = False

        while level and not found:
            next_level = defaultdict(list)

            for word in level:
                wordSet.discard(word)

            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]

                        if new_word in wordSet:
                            if new_word == endWord:
                                found = True
                            next_level[new_word].append(word)

            level = next_level

            for word in next_level:
                parents[word].extend(next_level[word])

        # Backtracking
        res = []

        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                dfs(p, path + [p])

        if found:
            dfs(endWord, [endWord])

        return res