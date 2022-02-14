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
 * 	Compare between currentMax and max using Math.max and keep larger value
*/

class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max = 0, currentMax = 0;
        for (int n : nums) {
            max = Math.max(max, currentMax = n > 0 ? currentMax + 1 : 0);
        }
        return max;
    }
}
