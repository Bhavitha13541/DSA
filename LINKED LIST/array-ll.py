class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

arr = [10,20,30,40,50]

head = Node(arr[0])
current = head

for i in range(1, len(arr)):
    current.next = Node(arr[i])
    current = current.next

temp = head
while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next
print("Null")

# 10 -> 20 -> 30 -> 40 -> 50 -> Null