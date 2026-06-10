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

temp = head
if  head == None or   head.next == None:
  print("list is empty or has only one node")

while temp.next.next is not None:
  temp = temp.next
temp.next = None
temp = head

while temp is not None:
  print(temp.data, end=" -> ")
  temp = temp.next
print("Null") 


# 
# output:

# 10 -> 20 -> 30 -> 40 -> Null
