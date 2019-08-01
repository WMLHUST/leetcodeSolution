# codingl: utf-8
def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ''

    min_len = len(strs[0])
    for i in strs:
        if len(i) < min_len:
            min_len = len(i)

    max_com = -1
    for i in range(0, min_len):
        ch = strs[0][i]
        is_same = True
        for j in range(1, len(strs)):
            if strs[j][i] != ch:
                is_same = False

        if not is_same:
            break
        else:
            max_com = i
    if max_com == -1:
        return ''
    else:
        return strs[0][:max_com + 1]
