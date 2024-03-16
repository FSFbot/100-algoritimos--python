def restoreIpAddresses(s):
    def backtrack(s, tmp):
        if len(s) > (4 - len(tmp)) * 3:
            return
        if not s or len(tmp) == 4:
            if not s and len(tmp) == 4:
                res.append('.'.join(tmp))
            return
        for i in range(min(3, len(s))):
            cur = s[:i+1]
            if (cur[0] == '0' and len(cur) >= 2) or int(cur) > 255:
                continue
            backtrack(s[i+1:], tmp + [s[:i+1]])

    res = []
    backtrack(s, [])
    return res

print(restoreIpAddresses("010010"))
print(restoreIpAddresses("25525511135"))