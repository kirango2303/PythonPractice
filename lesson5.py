#coding=utf-8

#Từ điển (Dictionary)
#dictionaryA = {
    #"key": "value",
    #"name": "Quang",
    #"age": 18,
    #"school": "HnAms"
#}
#print(dictionaryA)

#truy cập vào từ điển, thay đổi từ điển bằng bốn các (CRUD)

#Truy cập
#print(dictionaryA["key"]) #value
#print(dictionaryA["name"]) #Quang

#Update:
#dictionaryA["name"] = "Minh Anh"
#print(dictionaryA["name"])

#read đọc qua các phần tử loop
#for x in dictionaryA: #in ra tất cả key
    #print(x)

#for x in dictionaryA: #in ra tất cả value
    #print(dictionaryA[x])


#Viết đầy đủ
#for x in dictionaryA.keys(): 
    #print(x)
#for x in dictionaryA.values():
    #print(x)

#for x in dictionaryA.items(): #in ra cả key cả value , ít khi dùng
  #  print(x)


#check "key" exist?, chỉ check được phần key không check được value
#if "name" in dictionaryA:
    #print("Yes")

#Add thêm vào từ điển:
#dictionaryA["class"] = "12A1"


#Delete item
#1. popitem (delete phần tử cuối)
#2. del dictionaryA["name"]

#dictionaryA.popitem()
#del dictionaryA["name"]
#print(dictionaryA)

#Đặt tên biến:
#cách 1: train_case: ngo_minh_anh (html) 
#cách 2: camelCase: ngoMinhAnh

#Bài tập:
#Look up (tra thuật ngữ nma)
nmaDictionary = {
    "ghet": "iu",
    "iu": "ghet",
    "ban_nay_xinh_nhi":"like thi lieu hon",
    "ukm": "cau vai",
    "ny":"code",
    "em bao": "anh chet roi",
    "em_ko_ghen_bao_h": "tat axit"
}
#Liên tục tra từ điển và thực hiện sau đây
#Nhập vào 1 cái key --> in ra translation ("Từ này có nghĩa là")
#Nhập vào 1 key không có sẵn --> nhập translation cho từ đó --> in ra "updated"
#sau đó in ra cả dictionary
jealous = True 
while jealous:
    lookup = input("Từ cần giải nghĩa ")
    if lookup in nmaDictionary:
        defi1 = nmaDictionary[lookup]
        print("Từ này có nghĩa là " + defi1) 
    elif lookup == "iu Quang":
        jealous = False 
    else:
        defi2 = input("Nghĩa của từ đấy là ")
        nmaDictionary[lookup] = defi2
        print(nmaDictionary)