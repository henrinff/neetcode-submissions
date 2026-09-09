class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         prevMap = {} # every element before the current element and mapping the value to the index

         for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
         