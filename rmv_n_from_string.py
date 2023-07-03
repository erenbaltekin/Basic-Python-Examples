# Write a program to remove characters from a string starting from zero up to n and return a new string.

def remove_chars(string,n):
    if n < len(string):
        print(string[n:(len(string))])
    else:
        print("N must be less than the length of the string.")


string = input("Give a string: ")
n = int(input("Character: "))
remove_chars(string,n)
