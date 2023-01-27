def checkpanagram(str):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char in str.lower():
            return True
        else:
            return False
        input_string=input("Enter choosen string here")
        if checkpanagram(input_string.lower())==True:
            print(input_string,"is a panagram")
        else:
            print(input_string,"is not a panagram")