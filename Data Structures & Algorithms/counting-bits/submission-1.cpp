class Solution {
public:
    vector<int> countBits(int n) {
        vector<int>output;
        for(int i = 0;i<n+1;i++){
            int count = 0;
            int temp = i;
            while(temp>0){
                if(temp & 1){
                    count++;
                } 
                temp>>=1;
            }
            output.push_back(count);
        }
        return output;
    }
};
