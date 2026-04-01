class Solution {
public:
    int climbStairs(int n) {
        int way1 = 1;
        int way2 = 2;
        if(n == 1){
            return way1;
        }
        if(n == 2){
            return way2;
        }
        if (n >= 3){
            for (int i = 3; i<=n;i++){
                int temp = way1 +way2;
                way1 = way2;
                way2 = temp;
            }
            return way2;
        }
        
    }
};
