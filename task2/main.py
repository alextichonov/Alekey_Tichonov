# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def task2(arr):
   average = sum(arr) // len(arr)
   count = 0
   for i in range(len(arr)):
    count += abs(arr[i] - average)
   return count
x = list(map(int, input().split()))
print(task2(x))