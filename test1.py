# coding=utf-8
# python 2
#print "Hello world"

#Variables 
x = "Hello Quang" #gán giá trị x 
y = 5 # gán giá trị y = 5

#print y

#Data Types # kiểu dữ liệu 
# # "MinhAnh": string # chuỗi kí tự trong 2 nháy kép 
# 92: int 
# true/false: bool #kiểu chỉ cho ra một giá trị đúng hoặc sai

# bool (1>2) #false

#python 3

#object:


#number1 = 15.1321
#print int(number1)
#print type(number)
 
# tạo ra 1 cái sẽ hiện ra tên em khi chạy

#z = raw_input("Hello, Whats your name") #giá trị của z là cái chuẩn bị nhập vào terminal
#print "My name is" + z

#hỏi 3 thông tin về bản thân: school, age, class

#school = raw_input ("Which school do you go to?")
#age = raw_input ("How old are you?")
#myclass = raw_input ("Which class are you in?")
#print "I am" + age + "I study at" + school + "and I am in" + myclass

#a = (((92 + 141) * 101) ** 3)/7
#b = a % 90 
#print b 

#a = (((2 ** float((1)/2)) + 4) ** 10) ** float((1)/3)
#print int(a)

#b = 10 ** (1/2)
##print b

# condition

#a = 10
#if(a>10):
    #print "bigger than 10"
#elif(a>20 and a < 30):
    #print "smaller than 30 bigger than 20"
# else if
#else:
    #print "smaller than 10"

#and: 
#or:
#not:


#Loop (vòng lặp)
#for i in range(0,50,2):
   # print i

#for i in range(101,200,2):
    #print i

#for k in range(20,-20,-2):
  #  print k

  # Tính tổng các số từ 1 đến 100
  #hint là sum = 0 --> mỗi 1 bòng lặp --> cộng 1 số vào sum = sum + a

#sum = 0 
 
#for i in range(1,101):
   # sum = sum + i
#print sum
#Tính tích từ 1 đến 20
#product = 1
#for i in range(1,21):
 #   product = product * i
#print product 

#while dùng khi không biết trước số kết thúc là số nào

#a = 1
#while a < 9:
    #print a --> in a ra
    #a+=1 # phải thay đổi giá trị a sao cho while hữu hạn

#a = 0
##sum = 0
#while a < 100:
    #a+=1
    #sum = sum + a
#print sum

#Interactive: người dùng nhập các thứ vào
#raw_input

#Nhập radius hình tròn --> kết quả area
#nhập năm sinh in ra tuổi (số tự nhiên)

#r = float(raw_input("Radius is"))
#S = (r**2) * 3.14
#print S

#yearborn = int(raw_input("I was born on"))
#age = 2020 - yearborn
#print age

#Bài tập: 

a = [1,2,3,4,5,6]
for x in a:
  print(x)