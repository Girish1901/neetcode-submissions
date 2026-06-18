class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i in range(len(nums)):
            num = nums[i]
            if num in s:
                return [s.get(num),i]
            else:
                comp=target-nums[i]
                s[comp]=i
        return [-1,-1]
