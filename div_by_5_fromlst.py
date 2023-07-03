# Iterate the given list of numbers and print only those numbers which are divisible by 5
Givenlist = [10, 20, 33, 46, 55]

i = 0
while i < len(Givenlist):  # len(Givenlist) instead of len[Givenlist]
    if Givenlist[i] % 5 == 0:  # Use modulus operator (%) to check divisibility by 5
        print(Givenlist[i])
    i += 1

