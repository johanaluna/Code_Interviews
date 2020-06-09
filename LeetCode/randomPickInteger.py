import random
class Solution:
    def __init__(self, w):
        self.w = w
        self.suma = sum(self.w[0][0])
        self.sumAdded = [sum(self.w[0][0][0:x:1]) for x in range(1, len(self.w[0][0])+1)]
        print(self.suma)

    def pickIndex(self):
        sln = []
        sln.append('null')
        i = 0
        while i < len(self.w)-1:
            rad = random.randint(1,self.suma)
            for j in range(len(self.sumAdded)):
                if rad <= self.sumAdded[j] :
                    sln.append(j)
            
            i += 1
        return sln

      

w = [[[1]],[]]
w = [[[1,3]],[],[],[],[],[]]
# Your Solution object will be instantiated and called as such:
obj = Solution(w)
param_1 = obj.pickIndex()
print(param_1)