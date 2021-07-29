class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        as_string = str(x)
        if as_string == as_string[::-1]:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(10))
    print(solution.isPalindrome(-101))