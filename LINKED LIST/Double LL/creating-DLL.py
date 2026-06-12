class Node:
  def __init__(self, data):
    self.prev = None
    self.data = data
    self.next = None



head = Node(1)
current = head

for i in range(2, 15):
  new_node = Node(i)

  current.next = new_node
  new_node.prev = current

  current = new_node

temp = head
print("null",end="<->")

while temp:
  
  
  print(temp.data, end="<->")
  temp = temp.next

print("null")








