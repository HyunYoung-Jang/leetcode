// Source : https://leetcode.com/problems/max-consecutive-ones/
// Author : HyunYoung Jang
// Date   : 2022-02-14
/*
 * Task
 * 	Given a binary array nums, return the maximum number of consecutive 1's in the array.
 * Example 1:
 * 	Input: nums = [1,1,0,1,1,1]
 * 	Output: 3
 * 	Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
 *
 * Example 2:
 * 	Input: nums = [1,0,1,1,0,1]
 * 	Output: 2
 *
 * Approach
 * 	Reset currentMax to 0 if n = 0
 * 	Otherwise increase currentMax by 1
 * 	Compare between currentMax and maxMax using max and keep larger value
 *
 * Runtime / Memory usage:
 * 	372 ms, faster than 69.10% of Python3 online submissions for Max Consecutive Ones.
 * 	14.4 MB, less than 64.28% of Python3 online submissions for Max Consecutive Ones.
*/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxMax = 0
        currentMax = 0
        for n in nums:
            if (n > 0):
                currentMax = currentMax + 1
                maxMax = max(maxMax, currentMax)
            else:
                currentMax = 0
        return maxMax
