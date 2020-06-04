"""
There are 2N people a company is planning to interview. 
The cost of flying the i-th person to city A is costs[i][0], 
and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such 
that exactly N people arrive in each city.
Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
"""
def twoCitySchedCost(costs):
    costDifferences = []
    total = 0
    for cityA, cityB in costs:
        total += cityA # sum A
        costDifferences.append(cityA - cityB)
    costDifferences.sort()
    biggest_diff= costDifferences[len(costs)//2:]
    total = total - sum(biggest_diff)
    return total
        


costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# costs = [[10,20],[30,200],[400,50],[30,20]]
print(twoCitySchedCost(costs))
#1859