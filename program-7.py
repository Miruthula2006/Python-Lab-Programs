#Python function that accepts a string and calculate the number of upper case letters and lower case letters
def count(s):
    upper_count = 0
    lower_count = 0
    for i in s:
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+= 1
    return upper_count,lower_count
string=input("Enter the String: ")
upper_count,lower_count=count(string)
print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")




















