class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> index;
        for(int i =0; i < nums.size();i++){
            for(int j = 0; j< nums.size(); j++){
                if(i != j && nums[i] + nums[j] == target){
                    index.push_back(i);
                    index.push_back(j);
                    return index;
                }
            }
        }
    }
};
