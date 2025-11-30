# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Function to insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} at end (list was empty)")
            return

        # Traverse to last node
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        print(f"Inserted {data} at end")

    # Display the linked list
    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        print("Linked List:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# --------------------------
# Main Program
# --------------------------
ll = SinglyLinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.display()
