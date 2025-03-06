class Solution:
    """
    121. Best Time to Buy and Sell Stock

    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """

    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit


if __name__ == "__main__":
    assert Solution().maxProfit([7,1,5,3,6,4]) == 5
    assert Solution().maxProfit([7,6,4,3,1]) == 0
    print("Success!")
