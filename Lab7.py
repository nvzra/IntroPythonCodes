def main():
    word= ""
    word = input("Enter a word to convert into pig latin AND reverse, or enter 'done' to stop: ")
    word= word.lower()
    while word != "done":
        newrd = convertToPigLatin(word)
        print (newrd)
        ver = reverse(word) #reverse extra credit
        print (ver)
        word = input("Enter a word to convert into pig latin or enter 'done' to stop: ")
        word= word.lower()
    rot = input("Enter a word to convert to ROT13 ")
    inp= rot13(rot)
    print (inp)


def reverse(wrd):
    newrd= ""
    for i in range(len(wrd)):
        newrd += wrd [len(wrd) - (i)-1]
    return newrd

def rot13(wrd): #extra credit
    newrd = ""
    wrd = wrd.upper()
    for i in range (len(wrd)):
        letter = (ord (wrd[i]) + 13)
        if letter > 90:
            letter += 6
        newrd += chr(letter)
    newrd = newrd.lower()
    return newrd
        

def findFirstVowel(wrd):
    for i in range(len(wrd)):
        if wrd[i] in ["a", "e", "i","o" ,"u"]: #wrd is entered by user, and for loop 5 times, checking vowel
            return i
    return -1 #if no vowels at all, just return -1

def convertToPigLatin(wrd):
    VIND = findFirstVowel(wrd) #shortcut
    newrd= ""
    if VIND == 0:#1st case, if it is 0 then vowel is the first letter
        for j in range (len(wrd)-1):
            newrd += wrd [j+1] #each time to th eloop ur adding character j to the new word
        newrd += wrd[0] #added vowel
        newrd += "way"
#three seperate cases
    elif VIND != -1:#2nd case where there is a vowel, not the first one
        for l in range (len(wrd)-VIND):
            newrd += wrd[l + VIND]
        for m in range (VIND):
            newrd += wrd[m]
        newrd += "ay"
    else:#no vowels, 3rd case
        return wrd
    return newrd

    
main()


