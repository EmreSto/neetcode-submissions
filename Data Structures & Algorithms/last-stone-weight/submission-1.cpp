class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        make_heap(stones.begin(), stones.end());
        while(size(stones)>=2){
            pop_heap(stones.begin(), stones.end());
            int first = stones.back(); stones.pop_back();
            pop_heap(stones.begin(), stones.end());
            int second = stones.back(); stones.pop_back();
            if (first != second){
                stones.push_back(first - second);
                push_heap(stones.begin(), stones.end());
            }    
        }
        return stones.empty() ? 0 : stones[0];

    }
};
