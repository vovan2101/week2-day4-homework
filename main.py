#exersise 1

numbers = [1, 3, 5, 7, 8]
new_list = []
for num in numbers:
    if num >= 0:
        new_list.append(num * -1)
print(numbers)
print(new_list)


#exersise 2
def nums(address):
    digitlist = []
    for i in address:
        if i.isdigit():
            digitlist.append(i)
    return digitlist
nums("123 Real Street, Apt. 2, Springfield, OR 43498")


#exersise 3

def digits_sum(digits):
    return (str(int(digits)+ 1))
digits_sum("123")
