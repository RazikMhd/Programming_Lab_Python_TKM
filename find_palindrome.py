def isPalindrome(word):
    wordArray = [x for x in word]
    length = len(word)

    count = 0
    palindrome = True
    while(count<length):
        if(wordArray[count]!=wordArray[((length-1)-count)]):
            palindrome = False
        count +=1

    if(palindrome):
        print(word+" is a palindrome.")
    else:
        print(word + " is not a palindrome.")
