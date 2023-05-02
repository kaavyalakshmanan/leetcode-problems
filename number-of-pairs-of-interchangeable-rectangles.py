class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:

        # O(n) time O(n) space

        count = defaultdict(int)

        for w, h in rectangles:
            count[(w/h)]+=1
            
        res = 0
        for k, v in count.items():
            j = v
            # this is a math thing
            # if v = 4 --> 4 * 3 gives us number of permutations (aka order doesnt matter)
            # but we don care about permutations, we care about combinations (aka order does matter)
            # so we need to get rid of duplicates, so we divide by 2
            res += (j * (j-1))//2

        return res


