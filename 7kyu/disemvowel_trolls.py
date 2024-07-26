def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range (0,len(vowels)):
        s = string_.replace(vowels[i], '')
    print(s)

disemvowel('saabooooppppiiiiiiis')