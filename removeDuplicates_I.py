# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # k = len(set(nums))
        # array_idx = 1
        # ptr_cur, ptr_next = 0, 1
        # while array_idx != k:
        #     if nums[ptr_cur] != nums[ptr_next]:
        #         nums[array_idx] = nums[ptr_next]
        #         array_idx, ptr_cur = array_idx + 1, ptr_next
        #         ptr_next = ptr_cur + 1
        #     else:
        #         while nums[ptr_cur] == nums[ptr_next]:
        #             ptr_next += 1
        #         nums[array_idx] = nums[ptr_next]
        #         array_idx += 1
        #         ptr_cur = ptr_next
        #         ptr_next = ptr_cur + 1
        # return k

        array_idx = 0
        for idx in range(1, len(nums)):
            if nums[idx] != nums[array_idx]:
                array_idx += 1
                nums[array_idx] = nums[idx]
        return len(nums[:array_idx+1])