class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        M = num // 1000
        num -= M * 1000
        for i in range(M):
            result += 'M'
        C = num // 100
        num -= C * 100
        if C <= 3:
            for i in range(C):
                result += 'C'
        elif C == 4:
            result += 'CD'
        elif C == 5:
            result += 'D'
        elif C < 9:
            result += 'D'
            for i in range(C-5):
                result += 'C'
        elif C == 9:
            result += 'CM'
        X = num // 10
        num -= X * 10
        if X <= 3:
            for i in range(X):
                result += 'X'
        elif X == 4:
            result += 'XL'
        elif X == 5:
            result += 'L'
        elif X < 9:
            result += 'L'
            for i in range(X-5):
                result += 'X'
        elif X == 9:
            result += 'XC'
        I = num // 1
        if I <= 3:
            for i in range(I):
                result += 'I'
        elif I == 4:
            result += 'IV'
        elif I == 5:
            result += 'V'
        elif I < 9:
            result += 'V'
            for i in range(I-5):
                result += 'I'
        elif I == 9:
            result += 'IX'
        return result
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(3))
    print(solution.intToRoman(4))
    print(solution.intToRoman(9))
    print(solution.intToRoman(58))
    print(solution.intToRoman(1994))