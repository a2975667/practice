class Solution:
    def reverseString(self, s):
        #return s[::-1]
        string = list(s)
        for i in range(len(string)):
            if i > len(string)/2:
                return "".join(string)
            tmp = string[i]
            string[i] = string[len(string) - i]
            string[len(string) - i] = tmp