from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)  # faster lookup
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])  # (current word, steps)

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordSet:
                        queue.append((newWord, steps + 1))
                        wordSet.remove(newWord)  # mark visited
        return 0

s = Solution()
print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  
print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])) 