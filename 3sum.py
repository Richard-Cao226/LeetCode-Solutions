from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = num + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    answers.append([num, nums[left], nums[right]])
                    left += 1
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
        return answers

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))
    print(solution.threeSum([]))
    print(solution.threeSum([0]))
    