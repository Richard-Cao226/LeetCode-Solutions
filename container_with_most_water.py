from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        greatest = (right - left) * min(height[left], height[right])
        while left != right:
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            greatest = max(greatest, (right - left) * min(height[left], height[right]))
        return greatest

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
    print(solution.maxArea([1,1]))
    print(solution.maxArea([4,3,2,1,4]))
    print(solution.maxArea([1,2,1]))