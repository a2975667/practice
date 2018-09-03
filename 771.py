class Solution:
    def numJewelsInStones(self, J, S):
        Jset = set(J)
        return sum(x in Jset for x in S)