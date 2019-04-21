def ha (word):
    word = word.lower()
    pronunciation = ""
    for index in range(len(word)):
        if index == (len(word)-1):
            if word[index] == "a":
                pronunciation += "ah-"
            if word[index] == "e":
                pronunciation += "eh-"
            if word[index] == "i":
                pronunciation += "ee-"
            if word[index] == "o":
                pronunciation += "oh-"
            if word[index] == "u":
                pronunciation += "oo-"
                
        else:
            if word[index] == "a":
                if word[index+1] == "i":
                    pronunciation += "ai-"
                elif word[index+1] == "e":
                    pronunciation += "eye-"
                elif word[index+1] == "o":
                    pronunciation += "ow-"
                elif word[index+1] == "u":
                    pronunciation += "ow-"
                else:
                    pronunciation += "ah-"
            elif word [index] == "e":
                if word[index+1] == "i":
                    pronunciation += "ay-"
                elif word[index+1] == "u":
                    pronunciation += "eh-hoo-"
                else:
                    pronunciation += "eh-"
            elif word[index] == "i":
                if word[index+1] == "u":
                    pronunciation += "ew-"
                else:
                    pronunciation += "ee-"
            elif word [index] == "o":
                if word [index+1] == "i":
                    pronunciation += "oyo-"
                else:
                    pronunciation +="oh-"
            elif word [index] == "u":
                if word[index+1] == "i":
                    pronunciation += "ooey-"
                else:
                    pronunciation += "ow-"
            elif word[index] in "p,k,h,l,m,n":
               pronunciation += word[index]
            elif word[index] == "w":
                if index == 0:
                    pronunciation += "v"
                elif word[index-1] == "a":
                    pronunciation += "w"
                elif word[index-1] == "i,e":
                    pronunciation += "v"
                elif word [index -1] == "u, o":
                    pronunciation +=  "w"
         
           
    return pronunciation


word = input("Enter a Hawaaian word to pronounce: ")
for aimen in range(len(word)):
    badword= False
    if word [aimen].lower() in ("aeioupkhlmnw' "):
        output = ""
    else:
        print("These characters are invalid Hawaiian characters! Here are the invalid letters.")
        badword = True
        print (word [aimen].lower())
if badword == False:
    print (ha(word)) 

secWord = input("Would you like to do another word or 'no' to exit: ")
while secWord.lower() != "no" and "n":
    badword = False
    secWord2 = input ("Enter away!")
    for aimen2 in range (len(secWord2)):
        if secWord2 [aimen2].lower() in ("aeioupkhlmnw' "):
            output2 = ""
        else:
            print("These characters are invalid Hawaiian characters! Here are the invalid letters.")
            print (secWord2 [aimen2].lower())
            badword = True
    if badword == False:
        print(ha(secWord2))

    secWord = input("Would you like to do another word or 'no' to exit: ")
    
    
#w after i: iw pronounced "v"
#w after e: ew pronounced "v"
#w after u: uw pronounced "w"
#w after o: ow pronounced "w"
# a: ah
# e: eh
# i: ej
# o: oh
# u: oo


# ai: eye
# ae: eye
# ao: ow
# au: ow


# ei: ay
# eu: eh-oo


# iu: ew

# oi: oyo


# u: ow
# ui: ooey
