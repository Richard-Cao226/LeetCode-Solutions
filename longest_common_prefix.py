from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        minLength = 200
        for word in strs:
            minLength = min(minLength, len(word))
        if minLength == 0:
            return ""
        result = ""
        i = 0
        while i < minLength:
            letter = strs[0][i]
            j = 1
            while j < len(strs) and strs[j][i] == letter:
                j += 1
            if j == len(strs):
                result += letter
            else:
                break
            i += 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))
    print(solution.longestCommonPrefix(["dog","racecar","car"]))