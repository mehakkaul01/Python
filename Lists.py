# Level 1 - Simple indexing
# Question 1: Predict the output of the code below before running it.

fruits = ["apple", "banana", "mango", "orange"]
print(fruits[0])
print(fruits[2])
print(fruits[-1])

# Output:
# apple
# mango
# orange


numbers = [100, 200, 300, 400, 500]

print(numbers[1]) 
print(numbers[-2]) 
print(numbers[4])

# Output:
# 200
# 400
# 500


student = ["Rahul", 20, True, "Python"]

print(student[0]) 
print(student[2]) 
print(student[-1])

# Output:
# Rahul
# True
# Python



a = ["India", "Japan", "USA", "France"]

print(a[0][0]) 
print(a[0][2]) 
print(a[1][1]) 
print(a[-1][-1])

# Output:
# I
# d
# a
# e




colors = ["red", "green", "blue"]

print(colors[1][0]) 
print(colors[2][2]) 
print(colors[-1][0])
print(colors[1][2])


# Output:
# g
# u
# b
# e




a = [ [10, 20, 30], [40, 50, 60], [70, 80, 90] ]

print(a[0]) 
print(a[1]) 
print(a[2])
print(a[0][1]) 
print(a[1][2]) 
print(a[2][0])

# Output:
# [10, 20, 30]
# [40, 50, 60]
# [70, 80, 90]
# 20
# 60
# 70




students = [ ["Rahul", 20], ["Priya", 21], ["Amit", 19] ]

print(students[0][0]) 
print(students[1][1]) 
print(students[2][0])


# Output:
# Rahul
# 21
# Amit




data = [ 100, "Python", [10, 20, 30], True, ["India", "Japan", "USA"] ]

print(data[1]) 
print(data[2][0])
print(data[2][-1]) 
print(data[4][1]) 
print(data[4][-1])

# Output:
# Python
# 10
# 30
# Japan
# USA




a = [ "Hello", [1, 2, 3], "India", [True, False, [100, 200, 300]] ]

print(a[0][1]) 
print(a[1][2]) 
print(a[2][3]) 
print(a[3][2][1])


# Output:
# e
# 3
# i
# 200



x = ["Python", [10, 20, 30], "India"]

print(x[0][0]) 
print(x[0][-1]) 
print(x[1][1]) 
print(x[2][2])


# Output:
# P
# n
# 20
# d




x = [ [1, 2], [3, 4], [5, [6, 7]] ]

print(x[0][1]) 
print(x[2][0]) 
print(x[2][1][0]) 
print(x[-1][-1][-1])

# Output:
# 2
# 5
# 6
# 7



x = [ "Hello", ["India", "Python"], [10, [20, 30, [40, 50]]], True ]

print(x[1][1][0]) 
print(x[2][1][2][1]) 
print(x[-2][1][1])


# Output:
# P
# 50
# 30




# Q1: List references
current_actions = ["line", "circle", "square"]
backup_actions = current_actions
current_actions.append("triangle")
print(backup_actions) 
# ['line', 'circle', 'square', 'triangle']
# Yes, it has "triangle": both names point to the same list in memory.



# Q2: Last 3 items
cart = ["shoes", "shirt", "watch", "hat", "belt", "socks"]
print(cart[-3:])  
# ['hat', 'belt', 'socks']

# Q3: Sorting
tags = ["banana", "Vipia", "apple", "cherry", "vipin"]
tags.sort()
print(tags)  
# ['Vipia', 'apple', 'banana', 'cherry', 'vipin']
# Capital letters have lower ASCII values (A-Z = 65-90) than small letters (a-z = 97-122), so they come first.


# Q4: Every 4th element
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[::4])  
# [0, 4, 8]



# Q5: Add to the beginning
notifications = ["Like", "Comment"]
notifications.insert(0, "New Follower")
print(notifications)  
# ['New Follower', 'Like', 'Comment']



# Q6: Innermost integer
log_data = ["Vipin", 25, "Jaipur", 302020, True, ["Test", 43, [23242, [234234]]]]
print(log_data[5][2][1][0])  
# 234234



# Q7: Append vs Extend
new_batch = [500, -20, 30]

ledger = [100, -50, 200]
ledger.append(new_batch)
print(ledger)  
# [100, -50, 200, [500, -20, 30]]



ledger = [100, -50, 200]
ledger.extend(new_batch)
print(ledger)  
# [100, -50, 200, 500, -20, 30]



# Q8: No loops allowed


my_list = [3, 5, 8, 5, 1, 9, 5]

print(my_list[-1])            
# last element -> 5


print(my_list[::-1])          
# reverse -> [5, 9, 1, 5, 8, 5, 3]


my_list.append(10)            
# add to end


print(len(my_list))           
# total elements -> 8


print(sum(my_list))           
# sum -> 46


print(max(my_list), min(my_list))  
# 10 1


print(my_list.count(5))       
# count of 5 -> 3


print(my_list[:3])            
# first three -> [3, 5, 8]


print("Python" in ["Java", "Python", "C++"])  
# True


my_list.clear()               
# empty the list


print(my_list)                
# []


