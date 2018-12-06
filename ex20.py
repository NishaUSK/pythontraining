for x in range (0, 11):
    x *= 2
    print(x)
print("------------------------------")

#using floor division and modulo
s=18
n=28.16
print(n//s)
print(n%s)
print("------------------------------")

#using the round function
u=28.12378161828
print(round(u,5))
print("------------------------------")

#calculating sum of list,tuples and dictionary
number = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8,
9.9]
print(sum(number))
print("------------------------------")

print(sum((8,16,64,512)))
print("------------------------------")

print(sum({-10: 'x', -20: 'y', -30: 'z'}))
