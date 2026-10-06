class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;  //slow pointer
        for (int i = 0; i < nums.length; i++){  //fast pointer  
            if (nums[i] != val) {      //If the nums is correct
               nums[k] = nums[i];      //place at k and increment k
               k++;    
            }
        }
        return k;
    }
}
