
word = input("Please enter a string : ")

try:
    assert word == "python"
    print("You entered the word 'python'")
except:
    raise Exception("Sorry, no words other than python allowed.")




