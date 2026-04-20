class Solution {
    public int missingNumber(int[] nums) {
        // 0 to 5 
        // 1
        // [0, 2 , 3 ,4, 5] = res1 
        // [0,1,2 ... 5 ] = res2 
        // res1 = 14
        // res2 = 15
        // res2 - res1

        int sum1 = 0;
        int sum2 = 0;
        // [0,1,2 ... 5 ] => res2 = sum1
        for(int i = 0; i <= nums.length; i++){
            sum1 += i;
        }
        // [0, 2 , 3 ,4, 5] = res1 = sum2 
        for(int i = 0; i < nums.length; i++){
            sum2 += nums[i];
        }

        return sum1 - sum2;
    }
}
