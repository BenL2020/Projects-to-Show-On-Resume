#Benjamin Lambright
#Experimental buy chart created to figure out what the best combinations of units to by in Axis & Allies Anneversary Edition, Axis & Allies & Zombies, and 
#any other edition where tanks cost 5 IPCs, artillery 4, and infantry 3.

#RESULTS of tests: https://docs.google.com/document/d/14XMF7NXhI7ju7bOPU15l58gKVZ59dneWQPDB6AMcj8s/edit?usp=sharing

#The following is the code I used to obtain the results

#first import necessary packages and variables
import numpy as np
from tabulate import tabulate

#from unit_stats import prices, values
prices = [3, 4, 5]
values = [2.5, 3.5, 4]
W, industry = 30, 8

#finds all the possible combinations of buys
#combination sum written by Arnab Chakraborty
class Solution(object):
   def combinationSum(self, candidates, target):
      result = []
      unique={}
      candidates = list(set(candidates))
      self.solve(candidates,target,result,unique)
      return result
   def solve(self,candidates,target,result,unique,i = 0,current=[]):
      if target == 0:
         temp = [i for i in current]
         temp1 = temp
         temp.sort()
         temp = tuple(temp)
         if temp not in unique:
            unique[temp] = 1
            result.append(temp1)
         return
      if target <0:
         return
      for x in range(i,len(candidates)):
         current.append(candidates[x])
         self.solve(candidates,target-candidates[x],result,unique,i,current)
         current.pop(len(current)-1)
ob1 = Solution()
possibilities = ob1.combinationSum(prices,W)
#print(possibilities)

#now that we have all the possible senarios, let's see which one has the highest average strength
def sums(possibilities):
    sums = []
    sum = 0
    #first we need to just plug in each unit type into the formula
    for list in possibilities:
        for i in list:
            if i == 4:
                sum = 3 + sum
            if i == 3:
                sum = 2.5 + sum
            if i == 5:
                sum = 4 + sum
    #now, we need to increase the score for each artillery(4) paired with an infantry(3)
        if list.count(3) < list.count(4):
            sum = (list.count(3)/2) + sum
        else:
            sum = (list.count(4)/2) + sum
        sums.append(sum)
        sum = 0
    return sums
sum = sums(possibilities)
#print(sum)

def rightBuy(sum, possibilities):
    #finally, we need to find all the maximum solutions
    top = max(sum)
    tops = [i for i, x in enumerate(sum) if x == top] #list comprehension written by Matthew D. Scholefield
    solutions = [possibilities[i] for i in tops] #this one is mine
    return solutions
solutions = rightBuy(sum, possibilities)
#print(solutions)

def totalRevisedBuyChart(a,b): #creates the best buy for every number between 3 and 41
    budget = [x for x in range(a,b)]
    masterList = []
    for b in budget:
        possibility = ob1.combinationSum(prices, b)
        sum = sums(possibility)
        solution = rightBuy(sum, possibility)
        for x in solution:
            x.append(str(b))
            masterList.append(x)
    table = [[x[-1], x.count(3), x.count(4), x.count(5), (len(x) - 1)] for x in masterList]
    buyChart = tabulate(table, headers=["budget","infantry","artillery", "tanks", "total"])
    return buyChart
#print(totalRevisedBuyChart(3,41))

def revisedBuy(budget): #might trash this, but this is charts
    remainder = budget % 7
    whole = (budget - remainder)/7
    if remainder == 0:
        buy = [budget, whole, whole, 0, (2*whole)]
    if remainder == 1:
        if whole > 2:
            art = whole - 2
        else: art = 0
        table = [[budget, whole + 3, art, 0, (whole+3+art)], [budget]] #continue this later
        buy = [[x[-1], x.count(3), x.count(4), x.count(5), (len(x) - 1)] for x in table]
    return buy

#print(revisedBuy(7))

def revisedBuyChart(budget):
    #makes a table of the solution list so it reads easier
    possibilities = ob1.combinationSum(prices, W)
    sum = sums(possibilities)
    solutions = rightBuy(sum, possibilities)
    table = [[budget, x.count(3), x.count(4), x.count(5), len(x)] for x in solutions]
    buyChart = tabulate(table, headers=["budget","infantry","artillery", "tanks", "total"])
    return table, buyChart
table, buyChart = revisedBuyChart(W)
#print(buyChart)

#in case the industrial capacity is limited
def limitedBuy(budget, industry):
    possibilities = ob1.combinationSum(prices, W)
    poslengths = [len(i) for i in possibilities]
    limitedBuy = [x for x in range(len(poslengths)) if poslengths[x] == industry] #meet the length criteria
    limitedPossibilities = [possibilities[x] for x in limitedBuy]
    limitedSum = [sum[x] for x in limitedBuy]
    limitedSolutions = rightBuy(limitedSum, limitedPossibilities)
    limitedTable = [[budget, x.count(3), x.count(4), x.count(5), len(x)] for x in limitedSolutions]
    limitedBuyChart = tabulate(limitedTable, headers=["budget", "infantry", "artillery", "tanks", "total"])
    return limitedTable, limitedBuyChart
limitedTable, limitedBuyChart = limitedBuy(W, industry)
print(limitedBuyChart)
