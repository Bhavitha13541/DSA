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


def insertAtHead(head, val):
  newNode = Node(val)
  newNode.next = head
  head = newNode
  return head 

head = insertAtHead(head, 5)

temp = head

while temp is not None:
  print(temp.data, end=" -> ")
  temp = temp.next
print("NULL")

# output:
# 5 -> 10 -> 20 -> 30 -> 40 -> 50 -> NULL
  