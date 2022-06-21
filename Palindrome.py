def isPalindrome(str):
    revStr = str[::-1]
    if (str == revStr):
        return True
    return False

str  = input("Enter a String: ")
result = isPalindrome(str)

if result == True:
    print("The String is Palindrome")
else:
    print("The String is not Palindrome")