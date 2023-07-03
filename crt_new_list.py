# Given a two list of numbers, write a program to create a new list such that the 
# new list should contain odd numbers from the first list and even numbers from the 
# second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

oddlist1 = []
evenlist2 = []

i = 0
while i < len(list1):
    if list1[i] % 2 != 0:
        oddlist1.append(list1[i])
    i += 1

i = 0  
while i < len(list2):
    if list2[i] % 2 == 0:
        evenlist2.append(list2[i])
    i += 1

print(f"oddlist1: {oddlist1}, evenlist2: {evenlist2}")












