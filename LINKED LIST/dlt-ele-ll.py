class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  # Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

# def removeElement(head, val):
#   if head is None:
#     return None
  
#   if head.data == val:
#     return head.next
  
#   temp = head
#   prev = None
  
#   while temp is not None:
#     if temp.data == val:
#       prev.next = temp.next
#       break
#     prev = temp
#     temp = temp.next

#   return head

# head = removeElement(head, 30)

# temp = head

# while temp is not None:
#   print(temp.data, end=" -> ")
#   temp = temp.next
# print("NULL")

# # output:

# # 10 -> 20 -> 40 -> 50 -> NULL

def removeElement(head, val):
  if head is None:
    return None
  
  if head.data == val:
    return head.next
  
  temp = head
  prev = None

  while temp is not None:
    if temp.data == val:
      temp.data = temp.next.data
      temp.next = temp.next.next
      break
    temp = temp.next

  return head

head = removeElement(head, 40)

temp = head

while temp is not None:
  print(temp.data, end=" -> ")
  temp = temp.next
print("NULL")


# output:
# 10 -> 20 -> 30 -> 50 -> NULL