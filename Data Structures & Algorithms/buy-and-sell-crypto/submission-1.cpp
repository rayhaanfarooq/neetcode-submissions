class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minSeen = prices[0];
        int curMax = 0;

        for (int price: prices) {
            minSeen = min(price, minSeen);
            curMax = max(curMax, price - minSeen);
        }

        return curMax;
    }
};
