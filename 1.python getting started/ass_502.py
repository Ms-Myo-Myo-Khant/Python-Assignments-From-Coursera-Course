largest=None
smallest=None

while True:
    num=input('Enter a number:')
    if num=="done":
        break
    try:
        number=int(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest=number
    elif smallest is None:
        smallest=number
    elif largest<number:
        largest=number
    elif smallest>number:
        smallest=number


print("Maximum is",largest)
print("Minimum is",smallest)
