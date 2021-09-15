from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        bestSum = nums[0] + nums[1] + nums[len(nums)-1]
        smallestDiff = abs(target - bestSum)
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = num + nums[left] + nums[right]
                currDiff = abs(target - sum)
                if currDiff < smallestDiff:
                    bestSum = sum
                    smallestDiff = currDiff
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    return target
        return bestSum

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumClosest([-1,2,1,-4], 1))
    print(solution.threeSumClosest([0,0,0], 1))
