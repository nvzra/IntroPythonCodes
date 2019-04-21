
#Aimen Ahmed CIS 1051

import PyPDF2

pdfFile = open('encrypted.pdf', 'rb') # rb = binary file
Reader = PyPDF2.PdfFileReader(pdfFile)
dicti = open('dictionary.txt', 'r')

for word in dicti.readlines():
    word = word.strip()
    if Reader.decrypt(word.lower()) == 1:
        print('A password match was found: ', str(word.lower()), '\nThe PDF is decrypted successfully.')
        break

    elif Reader.decrypt(word.upper()) == 1:
        print('A password match was found: ', str(word.upper()), '\nThe PDF is decrypted successfully.')
        break


dicti.close()
pdfFile.close()
