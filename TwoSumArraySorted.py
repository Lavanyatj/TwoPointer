# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list([int]):
        left =0
        right = len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return[left+1, right+1]
            elif numbers[left]+ numbers[right] < target:
                 left +=1
            else:
                right -=1
        return[-1,-1]
s  = Solution()
print(s.twoSum([2,7,11,15], 9))
