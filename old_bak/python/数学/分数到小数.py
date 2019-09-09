class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        is_negtive = False
        if (numerator>0 and denominator<0) or (numerator<0 and denominator>0):
            is_negtive = True
        numerator = abs(numerator)
        denominator = abs(denominator)

        zs = numerator // denominator
        numerator = numerator % denominator

        remain_map = {}

        cur_index = 0
        start_index = -1
        decimal_res = ''
        while numerator!=0:
            remain_tmp = numerator * 10 % denominator
            zs_tmp = numerator * 10 // denominator
            if (zs_tmp, remain_tmp) in remain_map.keys():
                start_index = remain_map[(zs_tmp, remain_tmp)]
                break
            else:
                decimal_res += str(zs_tmp)
                remain_map[(zs_tmp, remain_tmp)] = cur_index
                numerator = remain_tmp
                cur_index += 1

        if start_index!=-1:
            decimal_res = decimal_res[0:start_index] + '(' + decimal_res[start_index:cur_index] + ')' + decimal_res[cur_index:]

        if len(decimal_res)>0:
            res = str(zs)+'.'+decimal_res
        else:
            res = str(zs)

        if is_negtive:
            return '-'+res
        else:
            return res

print(Solution().fractionToDecimal(-50, 8))

