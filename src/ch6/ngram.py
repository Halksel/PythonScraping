def ngram(s, num):
    res = []
    slen = len(s) - num + 1
    for i in range(slen):
        ss = s[i:i+num]
        res.append(ss)
    return res

def diff_ngram(sa, sb, num):
    a = ngram(sa, num)
    b = ngram(sb, num)
    r = []
    cnt = 0
    for i in a:
        for j in b:
            if i == j:
                cnt += 1
                r.append(i)
    return cnt / len(a), r

a = "今日、渋谷で美味しいトンカツを食べた."
b = "渋谷で食べた今日のトンカツは美味しかった."

r2, word2 = diff_ngram(a, b, 2)
print(r2,word2)
r3, word3 = diff_ngram(a, b, 3)
print(r3,word3)
