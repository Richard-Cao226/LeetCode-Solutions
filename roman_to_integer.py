class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        s = s.replace('CD','CCCC')
        s = s.replace('CM','DCCCC')
        s = s.replace('XL','XXXX')
        s = s.replace('XC','LXXXX')
        s = s.replace('IV','IIII')
        s = s.replace('IX','VIIII')
        total = 0
        for c in s:
            total += symbols.get(c)
        return total
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("III"))
    print(solution.romanToInt("IV"))
    print(solution.romanToInt("IX"))
    print(solution.romanToInt("LVIII"))
    print(solution.romanToInt("MCMXCIV"))