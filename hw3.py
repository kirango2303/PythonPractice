# coding=utf-8

#5) Viết ra tất cả các số chia hết cho 5 hoặc chia hết cho 7 từ 1 đến 1000

for i in range(1,1001):
    if(i%7==0 or i%5==0):
        print((i),end=" ")

#6) Nhập vào 1 số (<999) in ra số đảo ngược của số đó (abc --> cba)

m = int(input("Số muốn chọn là:"))  #230
a = int(m/100) #a=2
c = m % (int(m/10))
b = (m - ((a*100)+c))/10
num = (c*100) + (b*10) + a 
print(int(num))

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
    for i in range(2,(num-1)):
        f0 = f1
        f1 = fn
        fn = f0 + f1
    print(fn)

#8)Viết các năm nhuận từ năm 0 đến năm 2020

for i in range(1,2021):
    if (i%4==0 and i%100!=0) or (i%400==0):
        print((i),end=",")