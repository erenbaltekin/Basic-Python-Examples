# Write a program to iterate the first 10 numbers and in each iteration, 
# print the sum of the current and previous number.

current = 0

previous = 0 
i = 0
while i < 11:
    current = int(input("Bir sayı giriniz: "))
    
    print(f"Current Number {current} Previous Number  {previous}  Sum:  {current+previous}")
    previous = current
    current = 0
    i += 1   
else:
    print("Finish")