# class Node:
#   def __init__(self,data):
#     self.next = None
#     self.data = data

# head = Node(1)
# current = head

# for i in range(2,6):
#   new_node = Node(i)

#   current.next = new_node
#   current = new_node

# stack = []

# temp = head

# while temp:
#   stack.append(temp.data)
#   temp = temp.next

# temp = head

# while temp:
#   temp.data = stack.pop()
#   temp = temp.next

# temp = head
# while temp:
#   print(temp.data, end="->")
#   temp = temp.next
# print("null")

# # output:
# # 5->4->3->2->1->null


                              #  OPTIMAL SOLUTION

class Node:
  def __init__(self, data):
    self.next = None
    self.data = data

head = Node(1)
current = head

for i in range(2,6):
  new_node = Node(i)

  current.next = new_node
  current = new_node



temp = head
prev = None

while (temp != None):

  front = temp.next
  temp.next = prev
  prev = temp
  temp = front

head = prev

temp = head

while (temp != None):
  print(temp.data, end="->")
  temp = temp.next
print("null")


# output:
# 5->4->3->2->1->null


