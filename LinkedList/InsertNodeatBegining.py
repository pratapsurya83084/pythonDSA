# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Function to insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)     # create new node
        new_node.next = self.head # link new node to old head
        self.head = new_node      # update head
        print(f"Inserted {data} at beginning")

    # Function to display the list
    def display(self):
        temp = self.head
        if not temp:
            print("List is empty")
            return
        print("Linked List:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ------------------------------
# Main Program
# ------------------------------
ll = SinglyLinkedList()

# Insert few nodes at beginning
ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_beginning(10)

# Display the list
ll.display()
