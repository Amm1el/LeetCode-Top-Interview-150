/*
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
*/ 

class Solution {
    public int removeDuplicates(int[] nums) {
        int right = 1;  //double pointer method
        for (int left = 1; left < nums.length; left++){
            if (nums[left] != nums[left - 1]){  //if the nums at left is not equal to the element before, then we have a unique number
                nums[right] = nums[left];   //in that case, move the unique element at right to left, or the second position in second case
                right++;    //increment right so that the next unique element will be after the others
            }
        }
        return right;
    }
}
