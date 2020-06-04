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