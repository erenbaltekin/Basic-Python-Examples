number = int(input("Bir sayı giriniz: "))
if number == int((str(number)[::-1])):
    print(f"Yes. {number} is palindrome number")
else:
    print(f"No. {number} is not palindrome number")







