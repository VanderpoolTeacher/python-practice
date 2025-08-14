import array

# array of integers
int_array = array.array('i',[10,20,30,40,50])
print("Integer Array:", int_array)

# array of floats
float_array = array.array('f',[1.4,2.5,3.6,4.8])
print("Float Array:", float_array)

# array of unicode characters
char_array = array.array('u', 'Jello')
print("Charater Array:", char_array)

# insert into an array
arr = array.array('i', [1,2,3,4,5,6])
print(arr)
arr.append(4)
arr.insert(1,5)
print(arr)

# delete from an array
arr.remove(2)
arr.pop(1)
print(arr)

# for loop traversing an array
for element in arr:
    print(element)

# while loop with arrays
print("While loop")
print(len(arr))
index = 0

while index < len(arr):
    print(arr[index])
    index += 1

for i in range(len(arr)):
    arr[i] += 5 # Increment each element by 5
    print(arr)