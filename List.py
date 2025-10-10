lst = ["apple", "strawberries", "bananas", "Mango" , "pineapple"]

print('length of the list is: ', len(lst))
print('1st item of the list: ', lst[0])
print('last item of the list: ', lst[-1])

lst.append("kiwi")
print("list after appened: ",lst)
lst.remove("bananas")
print("list after remove: ",lst)
lst.sort()
print("the sorted list",lst)
lst.pop(2)
print("list after pop: ",lst)
lst.reverse()
print("list after reverse",lst)
print("multiplication on the list:",lst*5)
print("sliced list",lst[2:5])