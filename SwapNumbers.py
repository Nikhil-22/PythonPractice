x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))

#1st Way
# temp = x
# x = y
# y = temp

#2nd Way
# x,y = y,x

#3rd Way
x = x + y
y = x - y
x = x - y

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))