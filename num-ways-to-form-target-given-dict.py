class Solution:
    def numWays(self, words: List[str], target: str) -> int:

        # we are given an array of strings, called words
        # we are given a target string 
        # we want to construct the target string using the strings in words
        # we want to go left to right and if we use an index in any of the words, we can only choose subsequent indices to the right of that index for any of the words

        # Step 1: since answer may be too large and we want to return mod, lt's save that in a variable
        mod = (10 ** 9) + 7

        # Step 2: precompute the count of each character at each index in words
        # key = (index of word, character at that index)
        # value = its count across all words
        count = defaultdict(int)
        for w in words:
            for i, c in enumerate(w):
                count[(i, c)]+=1

        # Step 3: define DFS function 
        # we will make use of caching to make algo efficient
        cache = {} # map (i, k) to num ways to build target

        # i = index of target
        # k = index of word
        def dfs(i, k):

            # Base case
            # We build the word
            if i == len(target):
                return 1

            # we ran out of characters and couldn't build word
            if k == len(words[0]):
                return 0

            # if already cached, return that
            if (i, k) in cache:
                return cache[(i, k)]

            # recursive/general case
            # we could either build the target word by including the characters at position k, or by not including 

            c = target[i]
            cache[(i, k)] = dfs(i, k+1) # skip kth position
            cache[(i, k)] += (count[(k, c)] * dfs(i+1, k+1))

            return cache[(i, k)] % mod

        return dfs(0, 0)




