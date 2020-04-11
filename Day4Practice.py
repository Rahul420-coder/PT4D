list1 = [10, 12, 5, 6]

list2 = []

for item in list1:
    list2.append (item*item)
    
print (list2)

#list comrehension
[item*item for item in list1]

list1 = [10, 20, 30, 40]

list2 = [item+1 for item in list1]


list1 = ['Amar', 'Akbar', 'Anthony']

for item in list1:
    print (len(item))


[len(item) for item in list1]




list1 = [1,2,3,4,5]

def f1(x):
    return x**3

f1(list1[0])
f1(list1[1])
f1(10)

list(map(f1, list1))

list(map(lambda x: x**3, list1))


list1 = ['Amar', 'Akbar', 'Anthony']


def f2(str1):
    return len(str1)

list(map(f2, list1))

#anonymous functions
list(map(lambda str1: len(str1), list1))



list1 = [10, 20, 30, 40]

def f3(x):
    return x+1

list(map(f3, list1))

list(map(lambda x: x+1, list1))



list1 = [10, 3, 5, 12, 16]

def f4(x):
    if x > 10:
        return True
    else:
        return False

list(filter(f4, list1))


list1 = ['Jaipur', 'Udaipur', 'Kota','Bikaner']


def f5(str1):
    return 'pur' not in str1
        

list(filter(f5, list1))



list(filter(lambda str1: 'pur' in str1, list1))





#reduce

import functools

list1 = [1,2,3,4,5,6,7,8,9,10]

def f6(x, y):
    return x*y


functools.reduce(f6, [1,2,3,4,5,6,7,8,9,10])


map, redue is used in data  analytics

Hadoop - map, redude
Spark - map, reduce

[]

tuple1 = (1,2,3,4)
type(tuple1)

#tuple are read only




tuple1.index(4)


tp2 = (3,)
type(tp2)

print (tp2)



list1 = [1,2,3,4]
tuple(list1)

t = (1,2,3,5)
list(t)


lambda <input>:<return>

lambda x: x**2

lambda str1: 'pur' in str1


#Tuple are read only

tt = (1,2,3,2,2,4)

tt[0] = 10

tt.index(2)

tt.count(2)


tt = ('Raman', 2)

[(1,2,3),(10,20,30),()]


list(map(lambda name: len(name), 
    ['Ram','Shyam']))


name = "$Ram"
name = name[1:]