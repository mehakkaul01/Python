# Access elements: Given nums = [10, 20, 30, 40, 50], print the first element, the last element, and the middle element.

nums = [10, 20, 30, 40, 50]
print(nums[0])
print(nums[-1])
print(nums[2])


# Length and sum: Find the length, sum, minimum, and maximum of [4, 8, 15, 16, 23, 42].

a = [4, 8, 15, 16, 23, 42]
print(len(a))
print(sum(a))
print(min(a))
print(max(a))


# Append and insert: Start with fruits = ["apple", "banana"]. Add "mango" at the end and "orange" at index 1.

fruits = ["apple", "banana"]
fruits.append("mango")
fruits.insert(1, "orange")
print(fruits)


# Remove items: From [1, 2, 3, 4, 5], remove the value 3 and then remove the last element using pop().

a = [1,2, 3, 4, 5]
a.remove(3)
a.pop()
print(a)


# Slicing: Given [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], print the first 3 elements, the last 3 elements, and every second element.

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[:3])
print(a[-3:])
print(a[::2])


# Reverse a list: Reverse [1, 2, 3, 4, 5] in two different ways (a method and slicing).

nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)

nums = [1, 2, 3, 4, 5]
print(nums[::-1]) 


# Membership check: Check whether 25 exists in [10, 20, 30] and print True or False.

nums = [10, 20, 30]
print(25 in nums)


# Concatenate and repeat: Join [1, 2, 3] and [4, 5, 6] into one list, then create a list that repeats [0, 1] four times.

a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)
print([0, 1] * 4)


# Count and index: In [1, 2, 2, 3, 2, 4], find how many times 2 appears and the index of its first occurrence.

nums = [1, 2, 2, 3, 2, 4]
print(nums.count(2))
print(nums.index(2))


# Sort a list: Sort [5, 2, 9, 1, 7] in ascending and then descending order.

nums = [5, 2, 9, 1, 7]
nums.sort()
print(nums)

nums = [5, 2, 9, 1, 7]
nums.sort(reverse=True)
print(nums)


# Given colors = ["red", "green", "blue", "yellow"], print the second element and the second-to-last element.

colors = ["red", "green", "blue", "yellow"]
print(colors[1])
print(colors[-2])


# Given nums = [5, 10, 15, 20, 25, 30], print the elements from index 2 to index 4.

nums = [5, 10, 15, 20, 25, 30]
print(nums[2:5])


# Given nums = [1, 2, 3, 4, 5, 6], print all elements except the first and last.

nums = [1, 2, 3, 4, 5, 6]
print(nums[1:-1])


# Given letters = ["a", "b", "c", "d", "e"], print every element starting from index 1, skipping one each time (b, d).

letters = ["a", "b", "c", "d", "e"]
print(letters[1::2])


# Change the third element of [10, 20, 30, 40] to 99.

nums = [10, 20, 30, 40]
nums[2] = 99
print(nums)


# Replace the first two elements of [1, 2, 3, 4, 5] with [100, 200] using slicing.

nums = [1, 2, 3, 4, 5]
nums[:2] = [100, 200]
print(nums)


# Start with an empty list items = []. Add "pen", "book", and "bag" using append().

items = []
items.append("pen")
items.append("book")
items.append("bag")
print(items)


# Given nums = [1, 2, 3], add 4, 5, 6 to the end in one step using extend().

nums = [1, 2, 3]
nums.extend([4, 5, 6])
print(nums)


# Insert "kiwi" at the beginning of ["apple", "banana", "cherry"].

fruits = ["apple", "banana", "cherry"]
fruits.insert(0, "kiwi")
print(fruits)


# Remove the item at index 2 from [10, 20, 30, 40] using pop(), and print the removed item.

nums = [10, 20, 30, 40]
nums.pop(2)
print(nums)


# Delete the first element of [7, 8, 9] using del.

nums = [7, 8, 9]
del nums[0]
print(nums)


# Empty the list [1, 2, 3, 4] using clear().

nums = [1, 2, 3, 4,]
nums.clear()
print(nums)


# Make a copy of [1, 2, 3] using copy(). Change the copy and show the original is unchanged.

nums = [1, 2, 3]
new_nums = nums.copy()
new_nums[0] = 99
print(new_nums)
print(nums)


# Find the average of [10, 20, 30, 40] using sum() and len().

nums = [10, 20, 30, 40]
average = sum(nums) / len(nums)
print(average)


# Find the difference between the largest and smallest values in [8, 3, 15, 6].

nums = [8, 3, 15, 6]
print(max(nums) - min(nums)) 


# Check whether "banana" is not in ["apple", "cherry", "mango"].

fruits = ["apple", "cherry", "mango"]
print("banana" not in fruits)


# Check whether two lists, [1, 2, 3] and [1, 2, 3], are equal. Then check [1, 2, 3] and [3, 2, 1].

a = [1, 2, 3]
b = [1, 2, 3]
c = [3, 2, 1]
print(a == b)   
print(b == c)


# Find the sum of only the first three elements of [4, 5, 6, 7, 8].

nums = [4, 5, 6, 7, 8]
print(sum(nums[:3]))


# Create a list [0, 0, 0, 0, 0] without typing each zero.

zeros = [0] * 5
print(zeros)


# Join ["Hello"], ["World"], and ["!"] into one list.

x = ["Hello"]
y = ["World"]
z = ["!"]
print(x + y + z)


# Check whether a list [4, 8, 15] is empty. Do the same for []. (Hint: len.)

p = [4, 8, 15]
q = []
print(len(p) == 0)
print(len(q) == 0)


# Print the first and last elements of a list in one line, e.g. [3, 6, 9, 12] gives 3 12.

p = [4, 8, 15]
q = []
print(len(p) == 0)
print(len(q) == 0)


# Given [9, 4, 7, 1], print the list sorted, the smallest, and the largest.

nums = [9, 4, 7, 1]
print(sorted(nums))
print(min(nums))
print(max(nums))


# Given nums = [1, 2, 3, 4, 5, 6], split it into two lists: the first three and the last three.

nums = [1, 2, 3, 4, 5, 6]
first = nums[:3]
last = nums[3:]
print(first)
print(last)


# Given [1, 2, 3, 4, 5], create a new list with the elements in reverse order, without changing the original.

nums = [1, 2, 3, 4, 5]
nums2 = nums.copy()
nums2.reverse()
print(nums)
print(nums2)


# Swap the second and third elements of [10, 20, 30, 40].

nums = [10, 20, 30, 40]
nums[1], nums[2] = nums[2], nums[1]
print(nums)


# Given [5, 3, 8], add the sum of the list as a new last element.

nums = [5, 3, 8]
nums.append(sum(nums))
print(nums)


# Given names = ["Sam", "Ana", "Raj"], print the length of the list and the number of times "Ana" appears.

names = ["Sam", "Ana", "Raj"]
print(len(names))
print(names.count("Ana"))