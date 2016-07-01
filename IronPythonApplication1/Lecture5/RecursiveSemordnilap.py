def semordnilap(str1, str2):
    if (len(str1) != len(str2)):
        return False
    if (len(str1) == 0) or (len(str2) == 0):
        return True
    #str2LastCharPosn = len(str2) -1
    if (str1[:1] != str2[len(str2)-1:]):
        return False
    else:
        return semordnilap(str1[1:], str2[:len(str2)-1])       

def semordnilapWrapper(str1, str2):
    #can't be less than 2 chars long
    if (len(str1) < 2) or (len(str2) <2):
        return False
    #must be same length
   # if (len(str1) != len(str2)):
      #  return False

    #cant be same word
    if (str1 == str2):
        return False

    return semordnilap(str1, str2)

print semordnilapWrapper('tact', 'cat')