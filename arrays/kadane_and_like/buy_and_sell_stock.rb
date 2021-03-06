# Approach 1: DP, For more detailed understanding
# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    return 0 if !prices || prices.size <= 1

    n = prices.size
    dp_sell = Array.new(n, 0)   # dp_sell[i] is the profits from selling on day i
    dp_buy = Array.new(n, 0)    # dp_buy[i] is the loss from buying on day i

    # dp_sell[i] = dp_sell[i - 1] or prices[i] - dp_buy[i - 1] do nothing or sell at today's price selling price - cost price
    # dp_buy[i] = dp_buy[i - 1] or 

    dp_sell[0], dp_buy[0] = 0, -prices[0]

    1.upto(n - 1) do |i|
        dp_sell[i] = [dp_sell[i - 1], prices[i] + dp_buy[i - 1]].max
        dp_buy[i] = [-prices[i], dp_buy[i - 1]].max
    end

    dp_sell[n - 1]
end

# Approach 2: Simpler looking soluton, using kadane algorithm
# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    n, max_profit, cur_profit = prices.size, 0, 0
    1.upto(n - 1) do |i|
        cur_profit = [0, cur_profit + prices[i] - prices[i - 1]].max
        max_profit = [cur_profit, max_profit].max
    end

    max_profit
end

# [7,1,5,3,6,4]

# mp = 0, cp = 0
# 1

# mp 0, cp 0
# 5
# cp = 4, mp = 4

# cp = 4, mp = 4
# 3
# cp = 2, mp = 4

# cp = 2, mp = 4
# 6
# cp = 5, mp = 5

# cp= 5, mp = 5
# 4
# cp = 3, mp = 5

# Approach 3: One pass
# public class Solution {
#     public int maxProfit(int prices[]) {
#         int minprice = Integer.MAX_VALUE;
#         int maxprofit = 0;
#         for (int i = 0; i < prices.length; i++) {
#             if (prices[i] < minprice)
#                 minprice = prices[i];
#             else if (prices[i] - minprice > maxprofit)
#                 maxprofit = prices[i] - minprice;
#         }
#         return maxprofit;
#     }
# }

# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# At most 1 transaction

# Time: O(n)
# Space: O(1)

# Approach 1: DP
# Approach 2: Kadane
# Approach 3: Simple One Pass
# Steps
# Max profit is when we buy when it is cheapest and sell when it is the costliest


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(max_profit([7,1,5,3,6,4]), 5)
assert_equal(max_profit([]), 0)
