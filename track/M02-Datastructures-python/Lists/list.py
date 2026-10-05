#index    0 1 2 3 4 5
num = [1,2,3,4,5,3]
print(num[-4:-1])
print(num[1:5])
print(num[3 : ])
print(num, type(num))
print(len(num))
print(num[3])

#using constructor
stu = list(1 ,2 ,3 ,4, True,"Abhi")
print(stu,type(stu))

#adding elements
num = [1,2,3,4]
num.append(6)
num.insert(0,3)
num.extend([ 10, 20, 30])
print(num)

#removing the elements
num.pop()
num.remove(3)
num.clear()
print(num)

#changing elements
num = [1,2,3,4,5,3]
num[5] = 6
num[1:4] = [20,30, 40]
print(num)

a = [1, 2, 3]
b= a.copy()
print(b.index(3))

x= [1, 3, 2]
print(x.sort())
print(x.reverse())

lst = [1, 3, 2]
lst.sort(reverse = True)
print(lst)