class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # The problem: given a beginWord and an endWord, and a wordList, what is the min number of transformations to transform beginWord to endWord, where a transformation means changing at most one character, and the transformations should come from wordList?
        # Aka, find the shortest path between 2 nodes
        # Aka GRAPH PROBLEM

        # The naiive approach for building the adjacency list:
            # Nested loop over wordList where we compare word to word and maybe use a helper to compare character to character
            # the good news is every word has the same length
            # The bad news is the time complexity would be O(n^2m) where n = len(wordList) and m = len(word)
            # This wont pass on leetcode
            
        # since m < n, we can change time complexity to O(n*m^2) to create adjacency list
        # to find shortest path, we use BFS whose time complexity will be O(n^2m)

        # To build the adjacency list, notice the following:
            # to transform hot to something else, it would look like:
                # *ot
                # h*t
                # ho*
            # to transform dot into something else, it would look like:
                # *ot
                # d*t
                # do*
            # both of these words have *ot in common
        # So adjacency list would look like:
            # {*ot: [hot, dot, lot]}
            # where key is a pattern and val is list of words that fir that pattern
        # The complexity of this:
            # go over every word in list = n
            # go over every character for a given word and try removing each character to find its neighbors = m
            # add each word to the list = m
            # hence, O(n*m^2) to build this adjacency list

        # then we do the bfs part where we start at beginWord, look at its neighbors and we find the shortest path by returning when we get to endWord
        # time complexity for bfs is:
            # number of edges is n^2
            # length of each word is m
            # hence its O(n^2m)

        # Base case: check if endWord is in wordList
        if endWord not in wordList:
            return 0

        # Initialize adjacency list
        # benefit of defaultdict: if we insert a new value for the first time, the default is going to be an empty list
        neighbors = collections.defaultdict(list)

        # append beginWord to the beginning of wordList since its not there
        wordList.append(beginWord)

        # build adjacency list
        for word in wordList:
            # For every word, find every possible pattern for that word
            for j in range(len(word)):
                # Go to every single pos in word and replace with *
                pattern = word[:j] + '*' + word[j+1:]
                # remember: the key is the pattern, the val is a list of words that fit that pattern
                # so we index into neighbors with the given pattern and append this word to that corresponding list
                neighbors[pattern].append(word)

        # now lets do the bfs stuff
        # to avoid revisitng same node twice, we make use of a visited set, initalize with beginWord since thats where we start
        visited = set(beginWord)

        # we also need a q since this is bfs
        q = collections.deque([beginWord])

        # this is what we return
        # initialize to 1 because trivially beginWord == beginWord and requires at most 1 transformation (or in this exaclty 0)
        shortestPath = 1

        # if we find the word, return shortestPath
        # if we dont find word, when loop finishes, return 0
        while q:
            for i in range(len(q)):
                currWord = q.popleft()
                if currWord == endWord:
                    return shortestPath
                for j in range(len(currWord)):
                    pattern = currWord[:j] + '*' + currWord[j+1:]
                    for n in neighbors[pattern]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
            shortestPath+=1


        return 0

        # O(n^2m) time O(n^2m) space
        

        

