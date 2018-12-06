#list

list=['red','yellow','green','white']
print(list)
print("-------------------------")

list[1]='pink'
print(list)
print("-------------------------")

print(list[0:3])
print("-------------------------")

print(list[2:])
print("-------------------------")

print(list[-3:-1])
print("-------------------------")

list.append('orange')
print(list)
print("-------------------------")

list.insert(0,'black')
print(list)
print("-------------------------")

list1=['purple','skyblue','blue']
list.extend(list1)
print(list)
print("-------------------------")

list.remove('black')
print(list)
print("-------------------------")

print(list.pop(3))
print(list)
print("-------------------------")

print(list.index('orange'))
print("-------------------------")

list.reverse()
print(list)
print("-------------------------")

print(list.count('red'))
print("-------------------------")

list2 = [x for x in range(10)]
print(list2)
print("-------------------------")

list3 = [x ** 2 for x in range(10) if x % 2 == 0]
print(list3)
print("-------------------------")

list4 = [x for x in range(10) if x % 2 == 0]
print(list4)
print("-------------------------")

list5 = [x ** 2 for x in range(10) if x % 2 == 0]
print(list5)
print("-------------------------")

list6 = []
for x in [20, 40, 60]:
    for y in [2, 4, 6]:
        list6.append(x * y)
print(list6)
