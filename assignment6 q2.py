def palindrome(string):
    rev_string=string[::-1]
    print(rev_string)
    if string==rev_string:
        print("Enter string is a palindrome")
    else:
        print("Entered string is not a palindrome")
        user_string=str(input("Enter a word,phrase or sentence:"))
        palindrome(user_string)