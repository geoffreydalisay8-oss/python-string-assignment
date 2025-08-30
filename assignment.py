

#1
def reversed(sentence):
    return sentence[::-1]
#2
def countvowel(vowel):
    count = 0
    vowels = "aAeEiIoOuU"
    for char in vowel:
        if char in vowels:
            count += 1
    return count
##3
def palindrome(sentence):
    sentence = sentence.lower()
    return sentence == sentence[::-1]
#4
def replaceword(sentence, old, new):
    return sentence.replace(old, new)

#5
def casetitle(sentence):
    return sentence.title()
#6
def splitwords(sentence):
    return sentence.split()

#7
def frequencycounter(sentence):
    text = sentence.lower().split()
    freq = {}

    for words in text:
        freq [words] = freq.get(words, 0 ) + 1
        return freq
#8
def swapwords(sentence):
    return sentence.swapcase()


while True:
    sentence = input("input your sentence or numbers: ")
    print("\n from 1-9 pick what operation: ")
    print("1. reversed the sentence")
    print("2. Count the vowels")
    print("3. check if palindrome")
    print("4. find and replace a word")
    print("5. Format(title case)")
    print("6. Split into words ")
    print("7. Word frequency counter")
    print("8. Swap case")
    print("9. Exit")

    choice = input("enter your choice: ")

    if   choice == "1":
        print("reversed : " , reversed(sentence))

    elif choice == "2":
        print("countvowel: " ,countvowel(sentence))
    elif choice == "3":
        print("is palindrome" ,palindrome(sentence) )
    elif choice == "4":
        old = input("enter your old sentence: ")
        new = input("enter your new sentence: ")
        result = replaceword(sentence, old, new)
        print("your new sentence has successfully change: ", result)
        
    elif choice == "5":
        sentence = casetitle(sentence)
        print("your format has been change: " , sentence)

    elif choice == "6":
        print("words been split like this :", splitwords(sentence))

    elif choice == "7":
            print("count words: " , frequencycounter(sentence) )

    elif choice == "8": 
        result = swapwords(sentence)
        print("your sentence has been swapped: ", result )
    
    elif choice == "9":
            print("Exiting...")
            break
    else:
        print("invalid choice")

   