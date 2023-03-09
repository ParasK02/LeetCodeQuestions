class Solution {
    public int pivotIndex(int[] nums) {
        int leftsum= 0;
        int rightsum= 0;

        for(int i = 0; i<nums.length;i++){
            leftsum = getsum(nums,0,i)-nums[i];
            rightsum = getsum(nums,i,nums.length-1)-nums[i];
            if(leftsum == rightsum){
                return i;
            }
        }
        return -1;
    }
    public int getsum(int[] num, int start, int finish){
            int sum = 0;
            for(int i = start; i<=finish; i++){
                sum += num[i];
              
            }
            return sum;
    }
}
