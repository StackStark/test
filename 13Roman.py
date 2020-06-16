class Solution:
    def romanToInt(self, s):
        size1 = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        spec2 = {'I': set(['V', 'X']),'X': set(['L', 'C']),'C': set(['D', 'M'])}
        num = 0
        prev = ''
        for a,b in enumerate(s):            
            if b in spec2.get(prev, set()):
                num += size1[b] - 2 * size1[prev]
            else:
                num += size1[b]
            prev = b        
        
        return num
num='IV'
helper = Solution()
print(helper.romanToInt(num))