class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        
        # O(v*n) time O(v*n) space
        
        if not votes:
            return ''
        
        # Step 1: Create defaultdict to store counts
        ranks = collections.defaultdict(lambda: [0] * len(votes[0]))
        
        # Step 2: Count votes
        for i in votes:
            for idx, l in enumerate(i):
                ranks[l][idx]-=1
                
        # Step 3: Sort ranks by cnt and key
        srts = dict(sorted(ranks.items(), key=lambda x: (x[1], x[0])))
        
        # Return srts as string
        return ''.join(srts)
        
