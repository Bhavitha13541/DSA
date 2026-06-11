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

def removeKthNode(head, k):
  if head == None:
    return head
  
  if k == 1:
    return head.next
  
  temp = head
  count = 0
  prev = None

  while temp != None:
    count += 1
    if count == k:
      prev.next = temp.next
      break
    prev = temp
    temp = temp.next

  return head

head = removeKthNode(head, 3)


temp = head

while temp is not None:
  print(temp.data, end=" -> ")
  temp = temp.next
print("NULL")


# output:
# 10 -> 20 -> 40 -> 50 -> NULL

