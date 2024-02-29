x = int(input("enter monthly income: "))
a = int(input('Enter the amount spent in food: '))
b = int(input('Enter the amount spent in travel: '))
c = int(input('Enter the amount spent in house_rent: '))

sum = a+b+c
if x > sum:
    diff = x - sum
    print('Your savings after expenditure = ',diff)
else:
    print('No savings all salary spent!!. = ',sum)
