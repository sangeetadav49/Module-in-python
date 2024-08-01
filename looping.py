#Program to check if a person can vote
age=int(input("enter age"))
if age>=18:
    print("person can vote")
else:
    print("person can't vote")
    
# To check the grade of a student
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=70 and avg<80):
    print("Grade: C")
elif(avg>=60 and avg<70):
    print("Grade: D")
else:
    print("Grade: F")
# Input a number and check if the number is positive, negative or zero and display an appropriate message
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")
# To print the first 10 natural numbers

print("====The First 10 Natural Numbers====")

for i in range(1, 11):
    print(i)
# To print the first 10 even numbers
maximum = 10

for number in range(1, maximum + 1):
    
    if number % 2 == 0:
        print(number)
# To print odd numbers from 1 to n
start, end = 4, 19

# iterating each number in list
for num in range(start, end + 1):
    
    # checking condition
    if num % 2 != 0:
        print(num, end = " ")

# To print the sum of the first 10 natural numbers
num = 11
sum = 0
for i in range(num+1):
  sum+=i
print(sum)
# Program to find the sum of all numbers stored in a list
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))
