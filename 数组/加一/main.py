# coding: utf-8
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    n = len(digits)
    addOne = True
    for i in range(0, n):
        j = n-1-i
        if digits[j]==9 and addOne:
            digits[j] = 0
        else:
            addOne = False
            digits[j] = digits[j]+1
            break

    if addOne:
        return [1]+digits
    else:
        return digits

test = [9, 9, 9]
res = plusOne(test)
print(res)
