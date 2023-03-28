import math

def digits_check() :
    digits = input("Enter 10 digits:")
    if digits[0:] == digits[::-1]:
        print("Yes, the string is a polynomial")
    else:
        print("No, the string is not a polynomial ")
def word_check() :
    word = input("Enter a word:")
    if word[0:] == word[::-1]:
        print("Yes, the word is a polynomial")
    else :
        print("Nu , cuvantul nu este un polindrom")
def propozitie_check():
    sentence = input("Enter the sentence:")
    clean_sentence = sentence.replace(" ", "")
    if clean_sentence[0:]== clean_sentence[::-1]:
        print("Yes, the sentence is a polynomial ")
    else:
        print("No, the sentence is not a polynomial ")

digits_check()
word_check()
propozitie_check()
