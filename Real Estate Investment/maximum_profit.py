#  File: maximum_profit.py

#  Description: This uses a knapsack to find how much max profit a real estate agent could receive from investments.
#               This data is provided in a file called houses.txt

#  Student Name: Julian Wearden

#  Student UT EID: jfw864

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 52604

#  Date Created: 11/27/2021

#  Date Last Modified: 11/28/2021

import sys


def knapsack(num_houses, money, prices, profit):
    if num_houses == 0 or money == 0:
        return 0
    if prices[num_houses - 1] > money:
        return knapsack(num_houses - 1, money, prices, profit)
    else:
        return max(profit[num_houses - 1] + knapsack(num_houses - 1, money - prices[num_houses - 1], prices, profit), knapsack(num_houses - 1, money, prices, profit))


def main():
    # The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)

    # The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)

    # The third line is a list of house prices in million dollar which is a list of \textit{integer numbers} (Consider that house prices can be an integer number in million dollar only).
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i in range(0, len(prices)):
        prices[i] = int(prices[i])

    # Fourth line is projected annual % increase
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i in range(0, len(increase)):
        increase[i] = float(increase[i])

    # Find profit from each house and put in array
    profit = []
    for i in range(num_houses):
        percentage = float(increase[i]) / 100
        homePrice = float(prices[i])
        profit.append(percentage * homePrice)

    result = knapsack(num_houses, money, prices, profit)

    result = round(result, 2)
    print(result)


main()
