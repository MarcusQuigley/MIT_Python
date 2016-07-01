def isVowel(char):
    return char.lower() in ('a', 'e', 'i', 'o', 'u')
        
def isVowel2(char):
    chr = char.lower()
    if chr == 'a' or chr == 'e' or chr == 'i' or chr == 'o' or chr == 'u':
        return True
    return False

print isVowel('a')
print isVowel('d')
print isVowel('A')