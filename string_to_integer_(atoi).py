class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ind = 0
        for i in range(ind, len(s)):
            if s[i] != ' ':
                ind = i
                break
        positive = True
        if s[ind] == '-':
            positive = False
            ind += 1
        elif s[ind] == '+':
            ind += 1
        digits = '0123456789'
        readDigits = ''
        for i in range(ind,len(s)):
            if s[i] in digits:
                readDigits += s[i]
            else:
                break
        if readDigits == '':
            return 0
        else:
            ind = 0
            for i in range(ind, len(readDigits)):
                if readDigits[i] != '0':
                    ind = i
                    break
            result = 0
            for i in range(ind, len(readDigits)):
                result *= 10
                result += int(readDigits[i])
            if not positive:
                result *= -1
            if result > pow(2,31) - 1:
                result = pow(2,31) - 1
            elif result < pow(2,31) * -1:
                result = pow(2,31) * -1
            return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.myAtoi("42"))
    print(solution.myAtoi("   -42"))
    print(solution.myAtoi("4193 with words"))
    print(solution.myAtoi("words and 987"))
    print(solution.myAtoi("-91283472332"))
    