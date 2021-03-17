word = input("Enter the word Python : ")

try:
    if(word != "python"):
        raise Exception("Entered word is not Python!")
    else:
        print("You entered the word 'python' !")
except Exception as e:
    print(e)

