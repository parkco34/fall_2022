#!/usr/bin/env python
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = []

for item in list1:
    list2.append(item)

print(f"\nAppending:\nFirst list: {list1}\nSecond list: {list2}\n")

list3 = [0, 1, 1, 2, 3, 5, 8, 13]
list4 = []

list4 = list4 + list3
print(f"\nConcatenating: \nFirst list: {list3}\nSecond list: {list4}")
