# name = input("Enter your Name : ")
# age = int(input("Enter our age : "))
# email = input("Enter your Email: ")
# add = input("Enter your Address: ")
# phone = input("Enter your Phone : ")
# print(f"My name is {name} I am {age} years old. And my email is {email} . I live in {add} and Contact me :{phone}")
# a = "5"
# b = "10"
# print (int(a) + int(b))
# a = 1.5
# b = 5
# print (a + b)
# eng = int(input("English : "))
# Nepa = int(input("Nepali : "))
# sci = int(input("Science:  "))
# soc = int(input("Social : "))
# Mat = int(input("Maths : "))
# sum = eng + Nepa + sci + soc + Mat
# per = (sum/500)*100
# print (f"The sum is : {sum} and percent is {per}")
   
# p = int is : {Pr}")

# name = [
# [1, 2, 3, 4, 5]
# ]
# print (name[1])
# data = [
#     ["ram","sita",["hari"]],
#     ["ktm","pkr", "bkt",["pokhara"]]
# ]
# print (data[0][2][0])
# print(data[1][3][0])
# Users = []
# name = input("Enter your Name : ")
# email = input("Enter your Email : ")
# phone = input("Enter your Number : ")
# Users.append(name)
# Users.append(email)
# Users.append(phone)
# print (Users)
# name2 = input("Enter the next name : ")
# Users[0] = name2
# print(Users)


# data = {"one", "Two", "Three", "Four"}


# data1 = ["Five", "Six", "Seven", "Eight"]

# data.extend(data1)
# print(data)






# data = {
#     "name":"Sagar",
#     "age":22,
#     "add":{
#         "city":"Kathmandu",
#         "country" : [
#             "Nepal",
#             "India"
#         ]
#     } 
# }
# print(f"My name is {data['name']}")
# print (f"I live in {data['add']['city']}")
# print (f"I live in {data['add']['country'][0]}")
# data = {
#     "Play":"Play ok",
#     "Exit":"Exit ok", 
#     "option":{
#         "control":["Game control"," player control"],
#         "more" : ["Facebook","twitter"]
#              } 
#        }
# print (f"The condition is : {data['Play']}")
# print (f"The Option is {data['option']['control'][1]}")
# print (f"The Option is {data['option']['more'][1]}")






# age =int(input("enter your age: "))
# if age >= 18:
#     print("Elegible because you are above 18 years ")
# elif age <= 40:
#     print("Not elligible Because you are above 40 ")
# else: age <= 18 and age >= 40 
# print ("You are not Eligible because you are under 18 or above 40")


# data = [ 'One', 'Two', 'Three', 'Four', 'Five', 'Six' ]
# dat = []
# data.reverse(dat)
# print(dat)


# Looping

# a = 1
# while a<=5:
#     while a <= 5 and a>= 0:
#         print(a)
#     a = a+1
# a = a + 1

# i=0
# a=1
# print("Pattern")
# while a<=i and a>=5:
#     print(a)
# a+=1
    
# item = [1,2,3,4,5]

# for n in item:
#     print (dir(n))

# a = 0
# b = 0 
# while a > 1 and a < 5:
#     while b > 1 and b <= a:
#         print("*")
#         b = b + 1
#     a = a + 1
# for i in range (4):
#     for j in range(4):
#         print(j,end="")
#     print()

# for i in range(10):
#     for j in range (10-i):
#         print("*",end="")
#     print()

# info = {
# "name" : "Samyog",
# "Sub" : "Computer",
# "Grade" : 45
# }

# for i in info :
#     print(f"name is {info['name']}")
#     print()
# a = 0
# for i in range(10): 
#     a = i + a
#     print(a)
#     print()

# maths = 96
# science = 90
# social = 90
# english = 98  
# nepali = 97
# marks = maths + science + social + english + nepali
# gpa = float(((marks)/500*100)/25)
# print (f"Your total marks is : {marks} and you got {gpa}")
# if gpa < 4 and gpa > 3.2:
#     print ("You Got A+")
# elif gpa < 3.2 and gpa > 2.8:
#     print ("you got A ")
# elif gpa > 4 :
#     print("Invalid Marks ")
# else :
#     print("You Are Fail")



# age =int(input("Enter your age : "))
# if age > 18 and age < 40: 
#     if age > 18 and age < 25:
#         print("You can only dring coke")
#     else :
#         print("You can dring beer")
# else :
#     print("You cannot join the party")

# amt = 10000
# print ("Welcome to Samyog Bank")
# pin = int(input("Enter your Pin Code"))
# if pin == 123:
#     print(f"You have {amt}")
#     a = input(("Do you want to Withdraw [Y/N]"))
#     if a.lower()=="y":
#         amt2 = int(input("Enter the amount"))
#         print ("Thankyou you have withdrawl")
#         amt = amt - amt2
#         print (f"Current balance = {amt}")
#     else:
#         print("Thankyou")
# else :
#     print("Incorrect Pin : ")

# x = 7
# y = 82
# z = 10

# if x > y:
#     if x > z :
#         print("x is greater")
# if y > x:
#     if y > z:
#         print("Y is Greater")
# else:
#         print("Z is Greater")

# print("Enter your Name : ")

# a = input("Enter your name : ")
# foods = ['1. Momo', '2. Chowmin', '3. Swasage', '4. Pizza', '5. Biryani']
# print(f"Hello {a} Welcome to Our Resturant")
# print (f"Your Menue is : {foods}")
# print("What do u like : ")
# order = int(input()) 

# a = float(input("Enter 1st number : "))
# b = float(input("Enter 2nd number : "))
# c = float(input("Enter 3rd number : "))

# if a>b and a>c and b>c:
#     print(a,b,c) 
# elif b>a and b>c and c>a:
#     print(b,c,a)
# else :
#     print(c,a,b)

# users = [
#     ['ram', 'ram002'],
#     ['admin', 'admin002']
# ]

# username = input("Enter your Username : ")
# password = input("Enter your Password : ")

# if users[0][0] == username and users[0][1] == password:
#     print("Welcome")
# elif users[1][0] == username and users[1][1] == password:
#     print("Welcome")
# else:
#     print("Incorrect PAssword")


# student = [
#     {'name':'ram', 'age ': 20 },
#     {'name': 'shyam', 'age': 21}
# ]

# print(f"My name is {student[0]['name']}")
# print(f"My name is {student[1]['name']}")


# data = [
#     {'name': 'ram', 'gender': 'male', 'status': True,
#      "address": {
#          "country": "nepal",
#      }
#      },
#     {'name': 'sita', 'gender': 'female', 'status': True,
#      "address": {
#          "country": "pokhara",
#      }
#      },
#     {'name': 'laxmi', 'gender': 'female', 'status': True,
#      "address": {
#          "country": "kathmandu"
#      }
#      },
# ]
# print(f"Name is : {data[0]['name']} and Gender : {data[0]['gender']} and Address : {data[0]['address']['country']}")
# print(f"Name is : {data[1]['name']} and Gender : {data[1]['gender']} and Address : {data[1]['address']['country']}")
# print(f"Name is : {data[2]['name']} and Gender : {data[2]['gender']} and Address : {data[2]['address']['country']}")

# user = [
#     {'username':'admin', 'password':'admin123'},
#     {'username':'ram', 'password':'ram002'}
# ]

# username = input("Enter your UserName : ")
# password = input("Enter your Password : ")

# if username == user[0]['username'] and password == user[0]['password']:
#     print("Login Sussessful")
# elif username == user[1]['username'] and password == user[1]['password']:
#     print("Login Sussessful")
# else:
#     print("Incorrect Username or PAssword")


# a = int(input("Enter the Number : "))
# if a % 5 == 0 or a % 3 == 0:
#     print ("it is divisable")
# else:
#     print("It is not dvisible")

# b = int(input("Enter the table you want to know : "))
# a = b
# for i in range(1,11):
#     c = a * i 
#     print(f"{b} X {i} = {c}")



# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]
# odd = 0
# even = 0
# for i in number:
#     if i % 2 == 0:
#         print(f"{i} : Even")
#         even = even + 1
#     else:
#         print(f"{i} : odd")
#         odd = odd + 1 
# print(f"Even numbers are {even} and odd are {odd}")


# data = ['ram','sita','hari','gita','laxmi',]
# for i in data:
#     if i == 'ram'or i == 'laxmi':
#         print(i)
    
# data = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13,14,15]
# ]

# for i in range(3):
#     print(data[i][0])


# data = [
#     {'name': 'ram', 'age': 20,'gender':'male','status':True},
#     {'name': 'sita', 'age': 21,'gender':'female','status':True},
#     {'name': 'hari', 'age': 21,'gender':'male','status':True},
#     {'name': 'gita', 'age': 21,'gender':'female','status':False},
#     {'name': 'madan', 'age': 21,'gender':'male','status':False},

# ]
# a = len(data)
# print(f"Total People are : {a}")
# count = 0              
# for i in range(5):
#     if data[i]['status'] == True:
#         count = count + 1        
#         inac = a - count
# print(f"Total Active People : {count} ")
# print(f"The Inactive people : {inac} ")
# actmale = 0
# for j in range(5):
#     if data [j]['gender'] == "male" and data[j]['status'] == True:
#             actmale = actmale + 1
# print (f"Active Male : {actmale}")
# actfe = 0
# for j in range(5):
#     if data [j]['gender'] == "female" and data[j]['status'] == True:
#             actfe = actfe + 1
# print (f"Active female : {actfe}")

# iactmale = 0
# for k in range(5):
#     if data [j]['gender'] == "male" and data[j]['status'] == False:
#             iactmale = iactmale + 1
# print (f"inactive Male : {actmale}")
# iactfe = 0
# for k in range(5):
#     if data [j]['gender'] == "female" and data[j]['status'] == False:
#             iactfe = iactfe + 1
# print (f"Inactive female : {iactfe}")
  
# num = []
# a = int(input("Enter the number of Times : "))
# odd = 1
# even = 1
# while a > 1:
#     num = int(input("Enter the Number : "))
#     if num % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1
# print(f"Total odd is : {odd} and Even is : {even}")


# ######### Question - 1



# ############ Question - 2

# data = []
# num = int(input("Enter the number of times : "))
# for i in range(num):
#     b = int(input(" Enter Number : "))
#     data.append(b)

# newlist = [] 
# duplist = [] 
# for i in data:
#     if i not in newlist:
#         newlist.append(i)
#     else:
#         duplist.append(i) 
# print(f"Duplicates : {duplist}")


# ############### Question - 3  


# malecount = 0
# femalecount = 0
# num = int(input("Enter the numbers of people : ")) 
# for i in range(num):
#     name = input("Enter the Name : ")
#     gender = input("Enter The gender : ")
#     if gender == "male":
#         malecount = malecount + 1
#     else: 
#         femalecount = femalecount + 1
# print(f"Total males are {malecount} and total femals are {femalecount}")



# ############# Question - 4

# data = [1,2,3,4,8,5,3,6]
# data2 = []
# a = len(data)
# sum = 0
# for i in range(a):
#     if i % 2 == 0:
#         data2.append(data[i])
# for j in data2:
#     sum = j+sum
# print(sum)



# # ########### Question - 5

# students = ['ram','shyam','hari','sita','samyog','rawan']
# a = len(students)
# for i in range(a):
#     if i % 2 == 0:
#         print(students[i][0])
#     else:
#         print(students[i][-1])
  


# data = []           
# num = int(input("enter the number : "))
# for i in range(1,11):
#     c = num * i 
#     print(f"{num} X {i} = {c}")
#     data.append(c)

# for j in data:
#     if j % 2 == 0:
#         print(f"{j} is even ")


# num = int(input("Enter number of students: "))
# x = 1
# students_marks = []
# while x <= num:
#     for a in range(1):
#         nepali = int(input("Enter nepali marks: "))
#         english = int(input("Enter english marks: "))
#         computer = int(input("Enter computer marks: "))
#         math = int(input("Enter math marks: "))
#         science = int(input("Enter science marks: "))
#         total = nepali + english + computer + math + science
#         students_marks.append(total)
#     x += 1
# for mark in students_marks:
#     percentage = mark / 5
#     if percentage > 35 and percentage <= 45:
#         print("C")
#     elif percentage > 45 and percentage <= 60:
#         print("B")
#     elif percentage > 60 and percentage <= 80:
#         print("A")
#     elif percentage > 80 and percentage <= 100:
#         print("A+")
#     else:
#         print("Fail")
# students_marks.sort()
# highest = students_marks.pop()
# print(f"The Highest score is : {highest}")

# data = [
#     [
#         [1, 2, 3, 4, 5],
#         [11, 12, 13, 14, 15],
#         [81, 92, 93, 49, 95]
#     ]
# ]

# for i in range(5):
#     sum = 0
#     for j in range(3):
#         sum = data[0][j][i] + sum
#     print (sum)
# for row in data[0]:
#     row_total = sum(row)
#     row_highest = max(row)
#     print("Highest number in row: ", row_highest)
#     print("Total of row: ", row_total)

# data = [
#     {'name': 'ram', 'age': 20,'gender':'male','status':True},
#     {'name': 'sita', 'age': 21,'gender':'female','status':True},
#     {'name': 'hari', 'age': 21,'gender':'male','status':True},
#     {'name': 'gita', 'age': 21,'gender':'female','status':False},
#     {'name': 'madan', 'age': 21,'gender':'male','status':False},

# ]
# a = len(data)
# print(f"Total user : {a}")
# b = 0
# inactive_male = 0
# active_male = 0
# inactive_female = 0
# active_female = 0
# total_active = 0
# total_inactive = 0
# while b <= a:
#     if data[b-1]['status'] == True:
#         total_active = total_active + 1 
#     else:
#         total_inactive += 1
#     if data[b-1]['gender']== 'male':
#         if data[b-1]['status'] == True:
#             active_male += 1
#         if data[b-1]['status'] == False:
#             inactive_male += 1
#     else:
#         if data[b-1]['status'] == True:
#             active_female += 1
#         if data[b-1]['status']== False:
#             inactive_female += 1
#     b += 1
# print(f"Total Active : {total_active} ")
# print(f"Total Active Male  : {active_male} ")
# print(f"Total Active Female : {active_female} ")
# print(f"Total IN-Active Male : {inactive_male} ")
# print(f"Total IN-Active Female : {inactive_female} ")
# data = [
#     [1, 2, 3, 4, 5],
#     [11, 12, 13, 14, 15],
#     [81, 92, 93, 49, 95]
# ]
# a = 0
# while a < len(data):
#     print(data[a])
#     a += 1
# a = 1
# while a < 11:
#     b = 1 
#     while b < 11:
#         c = a * b
#         print(f"{a} X {b} = {c}")
#         b += 1
#     a += 1
# def addition(a,b):
#     c = a + b 
#     print(f"Addition : {c}")
# def subtraction(a,b):
#     c = a - b 
#     print(f"Subtraction : {c}")
# def division(a,b):
#     c = a / b 
#     print(f"DIvision : {c}")
# def multiplication(a,b):
#     c = a * b 
#     print(f"Multiplication : {c}")
# def mod(a,b):
#     c = a % b 
#     print(f"Modulas : {c}")
# a = int(input("Enter 1st number : "))
# b = int(input("Enter 2nd number : "))
# addition(a,b)
# subtraction(a,b)
# division(a,b)
# multiplication(a,b)
# mod(a,b)
# def total(numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print(sum)
# total([1,2,3,4,5,6,7,8,9,99])
# import random
# a = input("Enter Rock, Papper or Sissor : ")
# options = ['rock', 'papper', 'sissor']
# your = a.lower()
# print(f"Your : {your}")
# rand = random.randint(0,2)
# bot_option = options[rand]
# print("Computer :",bot_option)
# if bot_option == a.lower():
#     print("******* Match Draw ********")
# elif (bot_option == "rock" and your == "papper") or (bot_option == "papper" and your == "sissor") or (bot_option == "sissor" and your == "rock"):
#     print("***** You Won *****")
# elif (bot_option == "papper" and your == "rock") or (bot_option == "sissor" and your == "papper") or (bot_option == "rock" and your == "sissor"):
#     print("***** You Loose *****")
# else :
#     print("incorrect spelling")



# import random
# print("Welcome to Rock, Paper, Scissors!")
# choices = ["rock", "paper", "scissors"]
# player_choice = ""
# while player_choice not in choices:
#     player_choice = input("Choose rock, paper, or scissors: ").lower()
# computer_choice = random.choice(choices)
# print("The computer chose", computer_choice)
# if player_choice == computer_choice:
#     print("It's a tie!")
# elif player_choice == "rock" and computer_choice == "scissors":
#     print("You win!")
# elif player_choice == "paper" and computer_choice == "rock":
#     print("You win!")
# elif player_choice == "scissors" and computer_choice == "paper":
#     print("You win!")
# else:
#     print("The computer wins!")

# def area():
#     l = int(input("Enter Length :"))
#     b = int(input("Enter Breath :"))
#     return l,b

# def calculation(l,b):
#     are = l * b
#     return are
# l,b = area()
# area_of_rectangle = calculation(l,b)
# print(f"The area is {area_of_rectangle}")


# def get_rectangle_dimensions():
#     length = float(input("Please enter the length of the rectangle: "))
#     width = float(input("Please enter the width of the rectangle: "))
#     return length, width

# def calculate_rectangle_area(length, width):
#     area = length * width
#     return area

# length, width = get_rectangle_dimensions()
# area = calculate_rectangle_area(length, width)
# print("The area of the rectangle is:", area)



# def inputthevalue():
#     r = float(input("Enter the Radius : "))
#     return r
# def calculation(r):
#     perimeter = 3.14 * r * 2
#     return perimeter

# r = inputthevalue()
# area = calculation(r)
# print(f"Area is {area}")


