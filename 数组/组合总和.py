# coding: utf-8

# 更好的办法是dfs
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def doFunc(tar):
            res = []
            for item in candidates:
                if item == tar:
                    res.append([item])
                elif item<tar:
                    tmp_res = doFunc(tar-item)
                    # if tmp_res == None:
                    #     continue
                    for tmp_res_list in tmp_res:
                        tmp_res_list.append(item)
                        res.append(sorted(tmp_res_list))

            return res

        res = doFunc(target)
        return (set(tuple(x) for x in res))

cand = [2,3,5]
target = 8
Solution().combinationSum(cand, target)