class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lst = []
        for number in range(1,n+1):
            print(number)
            if number%3 == 0 and number%5==0:
                lst.append("FizzBuzz")
            elif number%3 == 0:
                lst.append("Fizz")
            elif number%5==0:
                lst.append("Buzz")
            else:
                lst.append(str(number))
        return lst