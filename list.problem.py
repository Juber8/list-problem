'''
#write a program to find sum of list
def sum(s):
    sum_no=1
    for i in s:
        sum_no= sum_no*i
    return sum_no
j=sum([10,20,30])

#write a program to find largst number of list:
#by using sort method
s=[10,20,30,40,50,60,70]
s.sort()
print('largest number of list:',s[-1])

#by using max method
s=[254,21,10,25585,235,2520,252,0,1,1,11,11,12,25]
print('largest number of list:',max(s))

#by taking input from user then find largest number of list and using function
def largest(list1):
    min=list1[0]
    for i in list1:
        if i>min:
            max=i
    return min
j=largest()

#by taking input from user

#sorted the list by incresing order of last element of touple
#a=
def last(n):
    return n[-1]
def sorted_list_last(touples):
    return sorted(touples,key=last)

print(sorted_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

tuple1 = [(8,3),(7,5),(6,2),(5,4),(4,1)]

list1=[]
list2=[]
for t in tuple1:
   list1.append(t[1])
list1.sort()
print(list1)
for j in list1:
   for q in tuple1:
        if j == q[1]:
           list2.append(q)
print(list2)

#remove duplicates from list
#by using set method
s=[10,10,20,10,30,50,50,40,50,80,4,]
s1=set(s)
print(s1)

s=[10,20,30,40,50,10,10,60,40,70,80,40,10,10,20,50]
s1=[]
for i in s:
    if i  not in s1:
        s1.append(i)
        print(i,end='',sep=',')

#by using function
data=[10,20,30,10,20,30,50,60,70,80,10]
def remove_diplicates(list):
    s=[]
    for i in data:
        if i not in s:
            s.append(i)
    return s
print(remove_diplicates(data))

#write a program to check wether list is empty or not
l=[1,2]
def check_list(l):
   if not l:
     print('list is empty')
   else:
     print('list has values')
j=check_list(l)
print(j)

#write a program to create a colne list
s=[0,20,30,4,40,50,60,7,10]
s1=s.copy()
print(s1)
print(s)



#check two list have common number or not
list1=[1,2,3,4,5,6]
list2=[10,11,12]
result=False
for x in list1:
    for y in list2:
        if(x==y):
            result= True
print(result)

def common_list(l1,l2):
    result= False
    for x in l1:
        for y in l2:
            if(x==y):
                result=True
    return result
print(common_list([1,2,3,4,5],[1,2,3,4,5]))

#set method to find common number
l1=[1,2,3,4,5]
l2=[1,2,3,4,5]
set1=set(l1)
set2=set(l2)
set3=set1.intersection(set2)
if len(set3)==0:
    print('list do not hav any comman valus')
else:
    print('common value')

#

#write a program to find to find list of word that are longer than n giver from user;
def findlargest_num(n,str):
    l=[]
    word=str.split()
    for i in word:
        if len(i) > n:
            l.append(i)
    return l
print(findlargest_num(4, "The quick brown fox jumps over the lazy dog"))

#remove 0 4 and 5th index elment
my_list=['juber','mulla','wasim','tasmiya','irfan','amit']
my_list=[x for (i,x) in enumerate(my_list) if i not in (0,4,5)]
print(my_list)

#check two list have common number or not
list1=[1,2,3,4]
list2=[5,6,7,8]
result=False
for i in list1:
    for j in list2:
        if (i==j):
            result=True
print(result)

#removing even number for removing even number out odd number codition
num = [7,8, 120, 25, 44, 20, 27]
num=[x for x in num if x%2!=0]
print(num)

num = 'juber','mulla''tasmiya','wasim'
j=(tuple(enumerate(num)))
print(j)

#shuffle list
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)

#wap to get first and last five number square
l=[]
for i in range(1,21):
    l.append(i**2)
print(l[:5])
print(l[-5:])

#Generate all permutations of a list in Python
import itertools
print(list(itertools.permutations([1,2,3])))

#find diffrence value from list
l1=[1, 3, 5, 7, 9]
l2=[1, 2, 4, 6, 7, 8]
output=list(set(l1)-set(l2))
print(output)

#wap to get index of all number in list
nums = [5, 15, 35, 8, 98]
print(list(enumerate(nums,start=0)))

nums = [5, 15, 35, 8, 98]
for nums_index , nums_value in enumerate(nums):
    print(nums_index,nums_value)

#convert list of word in to string
s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)

#find index of list
num =[10, 30, 4, -6]
print(num.index(30))

#remove 0 4 and 5 index of elment from list
my_list=['juber','mulla','wasim','tasmiya','irfan','amit']
my_list=[x for (i,x) in enumerate(my_list) if i not in (0,4,5)]
print(my_list)

s='juber'
print(list(enumerate(s)))

n=int(input('enter no of elemnts'))
l=[]
for i in range(1,n+1):
    j=int(input('enter element:'))
    l.append(j)
print(l)
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print('even list',even)
print('odd list:',odd)

l=[10,20,30,40,50,10,60]
l1=[54,98,25,2,366,5,25,45]
print(sorted(l+l1))

n=int(input('how many no u want in 1st list'))
l1=[]
for i in range(1,n+1):
    l=int(input('enter the elment:'))
    l1.append(l)
n2=int(input('how many no u want in st list'))
j=[]
for i in range(1,n2+1):
    d=int(input('enter the elemnet'))
    j.append(d)
print(sorted(l1+j))

s=input('enter your string:')
s1=s.split()
s2=sorted(s1,key=len)
print(s2[-1])
print(len(s2[-1]))

s=input('enter the string:')
s2=input('enter the string:')
if sorted(s)==sorted(s2):
    print('True')
else:
    print('False')

s = input('Enter original string')

p = input('Enter your string to check')
if set(p).issubset(set(s)):
    print('True')
else:
    print(False)

s='this is machine test'
jm=s.split()
print(jm)

s=input('enter the string:')
s2=input('enter the string:')
if sorted(s)==sorted(s2):
    print('True')
else:
    print('False')
s=input('enter ur string')
p = input('Enter your string to check')
if set(p).issubset(set(s)):
    print('True')
else:
    print(False)

l=[100,20,30,40,20,50,80]
l1=[200,50,60,70,90]
#print(l>l1)
j='zuber'
s='shubham'
print(j>s)
'''
