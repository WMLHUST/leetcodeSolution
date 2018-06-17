class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_char_dir = {}
        t_char_dir = {}

        for c in t:
            t_char_dir[c] = t_char_dir.get(c, 0) + 1

        left = -1
        right = -1
        cur_len = len(s)

        cur_left = 0
        cur_right = 0
        if s[0] in t_char_dir:
            s_char_dir[s[0]] = 1

        while cur_left <= cur_right < len(s):
            # 子串长度不够，扩充右边
            if cur_right-cur_left+1 < len(t):
                # 已经在最右了
                if cur_right == len(s)-1:
                    break

                cur_right += 1
                while cur_right<len(s) and s[cur_right] not in t_char_dir:
                    cur_right += 1

                if cur_right == len(s):
                    break
                s_char_dir[s[cur_right]] = s_char_dir.get(s[cur_right], 0) + 1
            else:
                # 长度够了，是否包含t
                isValid = True
                for k, v in t_char_dir.items():
                    if s_char_dir.get(k, 0) < v:
                        isValid = False
                        break
                if isValid:
                    # 有效子串，更新结果，为了寻找更短的子串，left右移
                    tmp_len = cur_right - cur_left
                    if tmp_len < cur_len:
                        left = cur_left
                        right = cur_right
                        cur_len = right-left+1

                    if s[cur_left] in s_char_dir:
                        s_char_dir[s[cur_left]] = s_char_dir.get(s[cur_left]) - 1
                    cur_left += 1
                    while cur_left<=cur_right and s[cur_left] not in t_char_dir:
                        cur_left += 1
                else:
                    # 无效子串，right右移

                    # 已经在最右了
                    if cur_right == len(s) - 1:
                        break
                    cur_right += 1
                    while cur_right < len(s) and s[cur_right] not in t_char_dir:
                        cur_right += 1
                    if cur_right == len(s):
                        break
                    s_char_dir[s[cur_right]] = s_char_dir.get(s[cur_right], 0) + 1

        if left == -1:
            return ""
        else:
            return s[left:right+1]
