largest = None
smallest = None

while True:
    num = input('Enter a number: ')
    if num == 'Done':
        break
    try:
        intNum = int(num)

        if smallest is None:
            smallest = intNum
        elif intNum < smallest:
            smallest = intNum
        if largest is None:
            largest = intNum
        elif intNum > largest:
            largest = intNum
    except:
        print('Invalid input')
        continue

print('Maximum is', largest)
print('Minimum is', smallest)