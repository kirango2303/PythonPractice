#Bài tập:
#Bài 0: (ôn buổi trước): Tính tổng các chữ số của 1 số 
a = int(input("Your number?"))
sum = 0
while(a>0):
    b = a%10
    sum = sum + b
    a = a // 10 # // : floor division chia lấy thương (15 // 2 = 7)
print("The sum of all digits is " + sum)

#Exercise 1
#Given the following dictionary:
inventory = {
    "gold" : 500,
    "pouch" : ["flint", "twine", "gemstone"],
    "backpack" : ["xylophone", "dagger", "bedroll", "bread loaf"]
}
#Try to do the followings:
#Add a key to inventory called 'pocket'.
#Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
#Then .remove('dagger') from the list of items stored under the 'backpack' key.
#Add 50 to the number stored under the 'gold' key.

inventory["pocket"] = ["seashell","strange berry","lint"]
inventory["backpack"].remove("dagger")
inventory["gold"] = [int(inventory["gold"])]
inventory["gold"].append(50)
print(inventory)

#Exercise 2 [optional]:
#Create a new dictionary called prices using {} format like the example above.
#Put these values in your prices dictionary:
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

#Create another dictionary called stock using {}:
#Put these values in your stock dictionary
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

#Loop through each key in prices. For each key, print out the key along with its price and stock information. Print the answer in the following format:
#apple
#price: 2
#stock: 0

#pear
#price: 3
#stock: 15

for i in prices:
    print(i)
    print("price: " + str(prices[i]))
    print("stock: " + str(stock[i]))

#Let's determine how much money you would make if you sold all of your food.
#Create a variable called total and set it to zero.
#Loop through the prices dictionaries. For each key in prices, multiply the number in prices by the number in stock. Print that value into the console and then add it to total.
#Finally, outside your loop, print total.

total = 0
for m in prices:
    total = total + (prices[m] * stock[m])
print("The total value is: " + str(total))

