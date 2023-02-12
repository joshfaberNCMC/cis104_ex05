count = 0
total = 0.0

while True:
    value = input('Enter a number: ')
    if value == 'Done':
        break
    
    try: # I did need to watch the video to get the try and except working. I was trying to wrap it around the whole while loop
        fValue = float(value)
        count = count + 1
        total = total + fValue
    except:
        print('Bad data')
        continue
print(total, count, total / count)