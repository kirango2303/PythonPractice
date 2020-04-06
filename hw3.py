# coding=utf-8

#5) Viết ra tất cả các số chia hết cho 5 hoặc chia hết cho 7 từ 1 đến 1000

for i in range(1,1001):
    if(i%7==0 or i%5==0):
        print((i),end=" ")

#6) Nhập vào 1 số (<999) in ra số đảo ngược của số đó (abc --> cba)

#m = int(input("Số muốn chọn là:"))  #230
#a = int(m/100) #a=2
#c = m % (int(m/10))
#b = (m - ((a*100)+c))/10
#num = (c*100) + (b*10) + a 
#print(int(num))

#7) Nhập số n viết ra số Fibonacci thứ n

num = int(input("n là")) 
f0=0
f1=1
fn=1
if num < 0:
    print("Không thoả mãn")
elif num == 0 or num == 1:
    print("Số thứ n là 1")
else:
    for t in range(2,(num-1)):
        f0 = f1
        f1 = fn
        fn = f0 + f1
    print(fn)

#8)Viết các năm nhuận từ năm 0 đến năm 2020

for k in range(1,2021):
    if (k%4==0 and i%100!=0) or (k%400==0):
        print((k),end=",")

#Chữa bài 6:
#in các chữ số từ dưới lên
#lấy chữ số cuối --> xet % cho 10 liên tục

#a = int(input("Your number?"))
#rev = 0
#while(a>0):
    #b = a%10
    #rev = (rev * 10) + b
    #a = a // 10 # // : floor division chia lấy thương (15 // 2 = 7)
#print(rev)

# Giải thích 
#598
#b = 8
#reverse = 8
#b = 9 
#muốn reverse = 89
#b = 5
#muốn reverse = 895


a = int(input("Your number?"))
rev = []
while(a>0):
    b = a%10
    rev.append(b)
    a = a // 10 # // : floor division chia lấy thương (15 // 2 = 7)
for i in range(0,len(rev)):
    print(rev[i],end="")