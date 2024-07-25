# This time no story, no theory. The examples below show you how to write function accum:
#
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

# The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(st):
    k = 0
    res = '' #result
    for i in range (0,len(st)):
        res = res + st[i].upper()
        for j in range (0,k):
            res = res + st[i].lower()
        k = k+1
    print(res)

accum('abcde')