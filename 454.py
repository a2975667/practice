class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dct = {}
        for a in A:
            for b in B:
                tmp = a+b
                if tmp in dct:
                    dct[tmp] += 1
                else:
                    dct[tmp] = 1
        print(dct)
        counter = 0
        for c in C:
            for d in D:
                if -(c+d) in dct:
                    counter += dct[-(c+d)]
        return counter