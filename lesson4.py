# coding=utf-8
# #Array Mảng (List)
#a = [1,2,3,4,5,6]

#Luôn bắt đầu từ 0
#a[0] : số đầu tiên
#a[5] : số cuối (số thứ 6)

#print(len(a)) #len: số lượng phần tử
#a[i] i: index phần tử ở vị trí i+1

#print(b[2]) #in ra phần tử thứ 3 của b

#In ra tất cả các phần tử của mảng

#for i in range(0, len(a)): #0->5
    #print(a[i],end=" ")

#print(a[-1]) #negative indexing -->6
#print(a[-2]) ra 5



 # CRUD: Create, Read, Update, Delete
 # read 
#a = [1,2,3,4,5,6]
#for x in a:
  #print(x)

#create thêm 1 phần tử mới
#a.append(7)
#a.append(8) thêm 1 giá trị vào
#a.extend([7,8]) thêm nhiều giá trị vào (vì thêm 1 mảng)
#print(a)

#delete

#C1: biết giá trị của phần tử đấy rồi
#b = ["shirt", "jeans", "hat", 1]
#b.remove("hat")
#print(b)

#C2: không biết giá trị của phần tử đấy
#dùng index
#b.pop(2) #nhớ là index phải trừ 1 đi (nhập 2 để xoá phần tử thứ 3)
#print(b)

#Update
#update phần tử index i -> thay bằng phần tử giá trị mới
#b[0] = "hat"
#shopping
#tủ đồ : ["make","clothes","sephora","croptop","offshoulder"]
#liên tục thực hiện các thao tác C, R, U, D
#nhập C: sau đấy nhập 1 đồ mới vào tủ đồ
#nhập R: in ra tủ đồ
#nhập U: nhập 1 index -> dổi giá trị của phần tử đấy thành cái khác
#nhập D: nhập 1 index --> xoá đi

#a.lower() #convert a --> lowercase
#a.upper() #convert a --> uppercase


#Bài tập:
#Đi shopping, trong tủ đồ có:
a = ["make","clothes","sephora","croptop","offshoulder"]
a.strip()

shopping = True
while shopping:
	command =(input("Enter an action"))
	if command == "R":
		print(a)
	elif command == "C":
		create =(input("What do you want to add?"))
		a.append(create)
		print(a)
	elif command == "U":
		update1 = int(input("Which index do you want to update?"))
		update2 = input("What do you want to update into?")
		a[update1] = update2
		print(a)
	elif command == "D":
		delete1 = int(input("Which index do you want to delete?"))
		a.pop(delete1)
		print(a)
	elif command == "S":
		shopping = False
	else:
		print("Invalid")


















