class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq;
        for(int i = 0; i < size(stones);i++){
            pq.push(stones[i]);
        }
        while(pq.size()>=2){
            int first = pq.top(); pq.pop();
            int second = pq.top(); pq.pop();
            int diff = first- second;
            if(first != second){
                pq.push(diff);
            }
        }
        if (pq.size()>0){
            return pq.top();
        }
        else{
            return 0;
        }

    }
};
