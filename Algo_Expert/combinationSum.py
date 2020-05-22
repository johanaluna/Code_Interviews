
# def combinationsSum(array, targetSum):
    
#     res = {}
#     def helper(arr, combination, total, required_sum, start):
#         if total > required_sum:
#             return
#         elif total == required_sum:
#             res[len(combination)]=combination
#             # print(self.res)
#             return
#         else:
#             for i in range(start, len(arr)):
#                 helper(arr, combination + [arr[i]], total + arr[i], required_sum, i)
#     helper(sorted(array), [], 0, targetSum, 0)
#     print(res)
#     return res


# array=[1,2,3,4,5]
# combinationsSum(array, 6)

def combinationSum(candidates, target) :
    def combination_sum(cur_ans, cur_sum, cand_idx):
        if cur_sum >= target:
            if cur_sum == target:
                if len(cur_ans)in ans:
                    ans[len(cur_ans)].append(cur_ans)
                else:    
                    ans[len(cur_ans)]=[cur_ans]
            return
        for i in range(cand_idx, len(candidates)):
            combination_sum(cur_ans + [candidates[i]], cur_sum + candidates[i], i+1)
    ans = {}
    combination_sum([], 0, 0)
    print(ans)
    return ans




array=[7,6,4,-1,1,2]
combinationSum(array,16)
combinationSum(array,7)
