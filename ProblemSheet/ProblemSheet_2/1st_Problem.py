# 1. Create a list and perform the following methods.
#   1) insert()
#   2) remove()
#   3) append()
#   4) len()
#   5) pop()
#   6) clear()

MyList = [10, 20, 30, 40]

MyList.insert(5, 50)  
print("After Insert : ", MyList)

MyList.remove(50) 
print("After Remove : ", MyList)

MyList.append(60)
print("After Append : ", MyList)

print("Length of MyList:", len(MyList))

popped_element = MyList.pop(1)
print(f"Element popped from index 1: {popped_element}")

MyList.clear()
print("After Clear:", MyList)
