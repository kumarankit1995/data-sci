#remove index 4 and add at position 2 and also at the end
ls = [54, 44, 27, 79, 91, 41]
a = ls.pop(4)
print(a)
print(ls)
ls.insert(2,a)
print(ls)
ls.append(a)
print(ls)

#given 2 list, create new with unique element
First_List=[2, 3, 4, 5, 6, 7, 8]
Second_List=[4, 9, 16, 25, 36, 49, 64]
third_list = First_List
third_list.extend(Second_List)
third = set(third_list)
third_lst = list(third)
print(third_lst)

#remve duplicate and find max and min
Original_list=[87, 52, 44, 53, 54, 87, 52, 53]
orig_set = set(Original_list)
orig_tup = tuple(orig_set)
print(orig_tup)
print(max(orig_tup))
print(min(orig_tup))

#disply each word in the string and count
b= "Welcome to Python"
cnt = 0
for i in b:
    cnt+= 1
    print(i,end='')
print(' ')
print('length of the string is ',cnt)

#Divisible by 7 and multiple of 5 between 1500 and 2700

for nu in range(1500,2701,1):
    if (nu%7==0) & (nu%5==0):
        print(nu,end=' ')


# Draw the diagram
n = 5
for i in range(n):
     print(i* '* ')
for j in range(n,0,-1):
    print(j* '* ')

#Count even and odd
even=0
odd=0
for i in range(1,11,1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print('Even count {} and odd count {}'.format(even,odd))

#Number between 100 and 400 having all digits as even
item =[]
for e in range(100,401,1):
    q =str(e)
    if (int(q[0])%2==0)and (int(q[1])%2==0) and (int(q[2])%2==0):
        item.append(q)
print(','.join(item))


# Max of the number

tu = (3,6,-5)
print(max(tu))

#Input number is prime or not

# inp = int(input('Enter the number : '))
# if inp>1:
#     for i in range(2,inp):
#         if (inp%i)==0:
#             print(inp,'is not a prime number')
#             break
#     else:
#         print('{} number is a prime number'.format(inp))


#Count upper and lower case in the string

# alpha =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# up = 0
# lw = 0
# st = input('Enter the string : ')
# for i in st:
#     if i in alpha:
#         lw+=1
#     elif (i.upper() in alpha):
#         up+=1
#     else:
#         print('Inputed is not a Alphabet')
# print('Number of upper case char is {} and number of lower case char is {}'.format(up,lw))


# Reverse the string
# sa = input('Input a string : ')
# print(sa[::-1])

