def longest(a1, a2):
    # your code
    res = ''.join(sorted(a1 + a2))
    a = ''
    for i in range (0,len(res)-1):
        if res[i] != res[i+1]:
            a = a + res[i]
    a = a + res[len(res)-1]
    return(a)