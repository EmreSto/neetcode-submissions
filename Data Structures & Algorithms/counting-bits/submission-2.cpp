class Solution {
public:
    vector<int> countBits(int n) {
        vector<int>output(n +1 , 0);
        for(int i = 0;i<n+1;i++){
            output[i] = output[i >> 1] + (i & 1);
        }
        return output;
    }
};
