def forward(s, t):
    r = dict()
    for _t_index, _t in enumerate(t):
        has_r = r.get(_t, "0")
        if has_r == "0":
            r[_t] = s[_t_index]
        else:
            if has_r != s[_t_index]:
                return 0
        pass

    r = dict()
    for _s_index, _s in enumerate(s):
        has_r = r.get(_s, "0")
        if has_r == "0":
            r[_s] = t[_s_index]
        else:
            if has_r != t[_s_index]:
                return 0
        pass
    return 1

S = input()
T = input()
result_count = 0
for i in range(len(S) - len(T) + 1):
    S = S[i: i + len(T)]
    result_count += forward(S, T)
    pass

print(str(result_count) + "\n")
