#coding=utf-8
# Bài tập:
#Bài 1: Làm ngược lại so với bài guessnumber
#Bài 2: Nhập 1 số n --> Kiểm tra một số có phải số nguyên tố hay không 
#Bài 3: Nhập n --> Tính 2nCn 
#Bài 4: nhập n --> kiểm tra có phải số chính phương không 
#Bài 5: Viết ra tất cả các số chia hết cho 5 từ 1 đến 1000
#Bài 6: Nhập vào 1 số <999 in ra số đảo ngược của số đó
#Bài 7: Nhập số n viết ra số Fibonacci thứ n

#hint bài 1: input mỗi lượt chơi ("Is" + (number) + "your number?") -> python3 viết là ("Is {} your number?".format(number)))
#làm thế nào để máy hỏi liên tục các số ở giữa --> dùng cách đặt low = mid/ high = mid 
#python3: print()

#Bài 1: Làm ngược lại so với bài guessnumber      
mid = 50
low = 0
high = 100        
playing = True
while playing:
    test_a = (input("Is {} your number, or bigger, or smaller?".format(mid)))
    if test_a == "yes":
        print("Win")
        playing = False 
    elif test_a == "smaller":
        low = mid
        mid = int((low + high)/2)
    elif test_a == "bigger":
        high = mid 
        mid = int((low + high)/2)



#Bài 2: Kiểm tra một số có phải số nguyên tố không
a = int(input("Số cần xét là"))
if a <= 2:
    print("Không phải số nguyên tố")
else:
    for b in range(2,a):
        c = a % b
        if c == 0:
            print("Không phải số nguyên tố")
            break
    else:
        print("Là số nguyên tố")


#Bài 4: Kiểm tra một số có phải số chính phương không 
p = int(input("Số cần xét là"))
import math
m = int(math.sqrt(p))
if (m * m) == p:
    print("Là số chính phương")
else:
    print("Không phải số chính phương")

#Bài 3: Nhập n --> Tính 2nCn 
#2nCn = (2n)! / n! * n! (tính: t!/k!*k!)
n = int(input("Giá trị của n là"))
q = (2 * n) + 1
k = 1
t = 1
for i in range(1,(n+1)):
    k = k * i
for r in range(1,q):
    t = t * r
C = (t) / (k * k)
print(C)

#Bài 5: Viết ra tất cả các số chia hết cho 5 từ 1 đến 1000
for i in range(1,1001):
    if (i % 5 == 0):
        print(i, end="")