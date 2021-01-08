#Leet Code - Richest Customer Wealth

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # variable to contain array of wealth of each customer
        wealth = []
        # iterate through accounts list
        for customer in accounts:
            # sum each list
            customer_wealth = sum(customer)
            # append to wealth list
            wealth.append(customer_wealth)
        # return max of wealth list
        return max(wealth)