class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int way1 = cost[0];
        int way2 = cost[1];
        int cheapest_cost =0;
        for(int i = 2; i<cost.size();i++){
            cheapest_cost = cost[i] + min(way1,way2);
            way1=way2;
            way2 = cheapest_cost;
        }
        return min(way1,way2);
        
    }
};
