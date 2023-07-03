# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

def check(lst):
    if lst[0] == lst[-1]:
        print(f"Given list {lst} \nresult is True")
    else:
        print(f"Given list {lst} \nresult is False")
    True    
list = [5,6,4,213,1,2,3,6,4,5]
check(list)


