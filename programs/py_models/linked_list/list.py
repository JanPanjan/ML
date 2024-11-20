from node import Node

class List:
    def __init__(self) -> None:
        self.head = None

    def insert(self, key: int):
        new_node = Node(key)

        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def search(self, key: int):
        cur = self.head

        while cur is not None:
            if cur.key == key:
                return True
            else:
                cur = cur.next
        
        return None

    def delete(self, key: int):
        cur = self.head

        if cur is not None and cur == key:
            self.head = cur.next
            return True
        
        while cur is not None:
            if cur.next is not None and cur.next.key == key:
                cur.next = cur.next.next
                return True
            else:
                cur = cur.next

    def pll(self):
        cur = self.head
        while cur is not None:
            print(cur.key, end=" -> ")
            cur = cur.next
        print("None")