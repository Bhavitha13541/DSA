class Node:
  def __init__(self,data):
    self.prev = None
    self.data = data
    self.next = None

head = Node(1)
current = head

for i in range(2,10):
  new_node = Node(i)

  current.next = new_node
  new_node.prev = current

  current = new_node

if head is None:
  print("null")

elif head.next is None:
  head = None

else:
  head = head.next
  head.prev = None

temp = head
print("null", end="->")

while temp:
  print(temp.data, end="<->")
  temp = temp.next
print("null")
     
# output:

# null->2<->3<->4<->5<->6<->7<->8<->9<->null
 