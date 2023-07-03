# Given two integer numbers return their product 
# only if the product is equal to or lower than 1000, else return their sum.

number1 = int(input("1.sayı: "))
number2 = int(input("2.sayı: "))

if number1*number2 <= 1000:
    print(f"The result is {number1*number2}")
else:
    print(f"The result is {number1+number2}")


