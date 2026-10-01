class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 2;  //start at 2 because no matter what the first two values will be correct
        for (int i = 2; i < nums.length; i++){  
            if (nums[i] != nums[k - 2]) {   //if the number is good / it is not repeated 3 or more times
                nums[k] = nums[i];  //doesnt matter first time through, but after will move     //update k with i / replace current with i
                k++;    //only increments k when the value is good
            }
        }
        return k;
    }
}
