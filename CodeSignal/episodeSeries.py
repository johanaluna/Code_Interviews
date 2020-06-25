from itertools import combinations 
def seriesEpisodes(duration, l, r, freeTime):
    """
    l = [0,  0,  1,  0,  3,  2]
    r = [2,  0,  3,  3,  3,  2]
    f = [62, 30, 60, 60, 32, 29]
    
    d = [30, 35, 32, 30]
    
    """
    i = 0
    totalDays = 0
    while i < len(l):
        episodes = duration[l[i]:r[i]+1]
        if l[i]==r[i] and duration[l[i]]==freeTime[i]:       
            totalDays += 1
            print(i, "1) totalDays",totalDays)
        elif sum(episodes)==freeTime[i]:
            totalDays +=1
            print(i, "2) totalDays",totalDays)
        elif r[i]> l[i]:
            result = [seq for i in range(len(episodes), 0, -1) for seq in combinations(episodes, i) if sum(seq) == freeTime[i]]
            if len(result)>0:
                totalDays +=1
                print(i, "3) totalDays",totalDays)
        i += 1
    return totalDays

duration= [30, 35, 32, 30]
l= [0, 0, 1, 0, 3, 2]
r= [2, 0, 3, 3, 3, 2]
freeTime= [62, 30, 60, 60, 32, 29]

print(seriesEpisodes(duration, l, r, freeTime))