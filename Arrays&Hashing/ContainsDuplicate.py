class Solution2:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # nested for loop to compare each value
         # nested loop must remain one index position ahead of i
         # compare each value as loop progresses

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        
        return False

        # T.C. = O(n) * O(n) = O(n^2)
        # S.C. = O(1)

# Trying to optimize the solution using Hash Set
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # use hash set to keep track of known values
         # if current index value exists in set, return True
         # else return False

        tracker = set()
         # for loop to iterate through nums
        for i in range(len(nums)):
            if nums[i] in tracker:
                return True
            else:
                tracker.add(nums[i])
        return False
        
        # T.C. = O(n)
        # S.C. = O(n)