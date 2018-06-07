'''*Q1*'''
l = []
limit = int(input('Enter number of elements: '))
print("Enter the list")
for i in range(0 , limit):
    listItem = input()
    l.append(listItem)
print(l)

'''Q2'''
l1 = ['google' , 'apple', 'facebook' , 'microsoft' ,'tesla']
l.extend(l1)
print(l)

'''Q3'''
print([[x,l.count(x)] for x in set(l)])

'''Q4'''
numList = []
limit1 = int(input('\nEnter number of elements: '))
print("Enter the list")
for i in range(0 , limit1):
    listItem1 = int(input())
    numList.append(listItem1)
print(numList)
numList.sort()
print(numList)

'''Q5'''
A=[]
B=[]
n1=int(input("Enter number of elements:"))
print("Enter the list")
for i in range(0,n1):
    b=int(input())
    A.append(b)
n2=int(input("Enter number of elements:"))
print("Enter the list")
for i in range(1,n2+1):
    d=int(input())
    B.append(d)
C = A+B
C.sort()
print("Sorted list is:",C)

'''Q6'''
stack = []
def push(stack):
    pushItem = input("Enter the item to be pushed :")
    stack.append(pushItem)
    print("Item Pushed")
    print(stack)
    pass
def pop(stack):
    n = stack[0]
    stack = stack[1:]
    print("Item popped")
    print(stack)
    pass

print("Enter your choice: \n    1. Push\n   2. Pop")
ch = int(input("Enter your Choice:" ))
if ch==1:
    push(stack)
elif ch==2:
    pop(stack)

'''Q7'''
testList = []
limit3 = int(input('Enter number of elements: '))
print("Enter the list")
for i in range(0 , limit3):
    listItem4 = int(input())
    testList.append(listItem4)
print(testList)
evenCounter = int(0)
oddCounter = int(0)
for x in testList:
    if (x % 2 == 0) :
        evenCounter += 1
    else:
        oddCounter += 1
print("Even elements : " )
print(evenCounter)
print("Odd elements : ")
print(oddCounter)