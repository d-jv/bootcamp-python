#1
def a():
    return 5
print(a())
#Print prediction: 5 Correct

#2
def a():
    return 5
print(a()+a())
#Print prediction: 10 Correct

#3
def a():
    return 5
    return 10
print(a())
#Print prediction: 5 Correct

#4
def a():
    return 5
    print(10)
print(a())
#Print prediction: 5 Correct

#5
def a():
    print(5)
x = a()
print(x)
#Print prediction: None Correct

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
#Print prediction: 3, then 5. Cant sum if nothing returns. Correct

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#Print prediction: 25 Correct

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
#Print prediction: 100, then 10 Correct

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) #7
print(a(5,3)) # 14
print(a(2,3) + a(5,3)) #21
#Print prediction: 7, 14, 21  Correct

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5)) 
#Print prediction: 8  Correct

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
#Print prediction: 500, 500, 300, 500  Correct

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#Print prediction: 500, 500, 300, 500 Correct

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
#Print prediction: 500, 500, 300, 300 Correct

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
#Print prediction: 1, 3, 2 Correct

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
#Print prediction: 1, 3, 5, 10 Correct