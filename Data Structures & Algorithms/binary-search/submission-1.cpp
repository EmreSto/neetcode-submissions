class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() -1;
        while (left <= right){
            int mid_index = (left + right) / 2;
            if(nums[mid_index] < target){
                left = mid_index +1;
            }
            else if (nums[mid_index] > target){
                right = mid_index -1;
            }
            else if (nums[mid_index] == target){
                return mid_index;
            }
        }
        return -1;
    }
};
