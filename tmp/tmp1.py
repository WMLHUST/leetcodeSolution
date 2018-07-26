n = input()
s = input()
s_ws = [int(x) for x in s.split()]
case_num = int(input())
for i in range(case_num):
    res = 0
    case = input()
    case_ws = [int(x) for x in case.split()]
    if case_ws[0]>case_ws[1]:
        print(0)
        continue
    for j in range(case_ws[0], case_ws[1]+1):
        if s_ws[j-1] == case_ws[2]:
            res += 1

    print(res)