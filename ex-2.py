# Write a function to sort the list based on the first letter of the second element

lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"),
     (1805832, "West Virginia"), (39865590, "California")]
lst = sorted(lst,key=lambda x:x[1])
print(lst)

# Write a function to sort the list based on the last letter of the second element

lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"),
     (1805832, "West Virginia"), (39865590, "California")]

lst = sorted(lst,key=lambda x:x[1][-1])
print(lst)

#Create a range from 1 to 8 merge the given list and together to create a new list of tuples.

lst1=["Energy", "Agriculture", "Industry", "Technology", "Finance", "Forestry", "Transport"]
ls2 = list(zip(lst1,list(range(1,8))))
print(ls2)

# Write a function and create a list consisted of the number of occurence of letter: a (all a's)

lst1=["Antartica", "America", "Armania", "Australia", "Albania", "Afganistan","Alaska"]
lst1= [i.lower() for i in lst1]
lst2 = list(map(lambda x:x.count('a'),lst1))
print(lst2)

# Write a function filter all the vowels in a given string using filter

str1="Inceptz is one of the best institutes to read data science in chennai"
# str2 = list(i for i in str1 if i.lower() in "aeiou")
# print(str2)

str2 = list(filter(lambda x: True if x.lower() in 'aeiou' else False,str1))
print(str2)

#Write a function to create a list as the square of elements from the given list if the square is greater than 60

lst1=[5, 6, 7 , 8, 9, 10, 12, 14]
lst3 = list(map(lambda x: x*x,lst1))
print(lst3)

# take the words given below as input and use reduce to make it a sentence
# import functools
# L = ['Inceptez ', 'provides ', 'the ', 'best ','inclass ' ,'trainings ','and ', 'is ', 'the ', 'best']
# ls = functools.reduce((lambda x,y:x+y),L)
# print(ls)


