from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        d = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    
        def backtrack(curr: str, currInd: int):
            if len(curr) == len(digits):
                res.append(curr)
                return
            for c in d[int(digits[currInd])]:
                backtrack(curr + c, currInd + 1)
        backtrack("", 0)
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("23"))
    print(solution.letterCombinations(""))
    print(solution.letterCombinations("2"))