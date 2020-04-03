#coding=utf-8
#thư viện: chỗ chứa rất nhiều lệnh tự viết ra ngoài các lệnh sẵn có
# from (thư viện) import (cái gì đó trong thư viện)
#from random import * 

#import * tức là lấy tất cả mọi thứ trong thư viện
#thư viện abc nếu chỉ lấy a
#from abc import a
#from abc import * (lấy tất cả abc)

#nếu không biết lấy hàm nào lên stackoverflow search

import random
number = random.randint(1,100)



playing = True 
while playing:
    a = int(raw_input("The number in my head is"))
    if(number < a):
        print "Smaller"
    elif(number == a):
        print "win"  
        playing = False
    else:
        print "Bigger"


#phải nhập liên tục số cho đến khi đoán đúng 
#nhập liên tục không biết dừng lúc nào
#--> dùng vòng lặp while 

#playing = True #đang chơi cái game này
#while playing == True: #khi đang chơi
    #nhập input đoán số máy tính nghĩ
 #   elif number == a:
  #  thắng rồi --> không chơi nữa
   # playing = False --> thoát vòng lặp ra