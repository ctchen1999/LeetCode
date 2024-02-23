class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.next_node = None
    
    def __repr__(self) -> str:
        return "<Node> data: {}".format(self.data)

class linked_list():
    def __init__(self) -> None:
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def add(self, data):
        """
        Add a new node at the beginning
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current =  current.next_node
        return count
    
    def search(self, key):
        """
        Search for a given key
        
        Takes O(n) -> like linear search
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        """
        Insert a new node into the index position
        Insert a new node takes O(1) time but finding the insert position takes O(n).
        
        Takes O(n) time    
        """
        insert_node = Node(data)
        current = self.head
        
        if index == 0:
            self.add(data)
        else:
            # 找insert 位置的前後node
            for _ in range(index-1):
                current = current.next_node
            prev_node = current
            next_node = current.next_node
            
            prev_node.next_node = insert_node
            insert_node.next_node = next_node
    
    ## First version of remove
    # def remove(self, key):
    #     current = self.head
    #     found = False
    #     previous_node = None
    #     while current and not found:
    #         if current == self.head and current.data == key:
    #             found = True
    #             self.head = self.head.next_node
    #         elif current.data == key:
    #             found = True
    #             previous_node.next_node = current.next_node
    #         else:
    #             previous_node = current
    #             current = current.next_node
    #     return current 
    
    ## Second version of delete
    def remove(self, index):
        current = self.head
        if index == 0:
            self.head = current.next_node
        else:
            for _ in range(index-1):
                current = current.next_node
            prev_node = current
            tmp = current.next_node
            next_node = tmp.next_node
            
            prev_node.next_node = next_node
        return current
            
        
    def __repr__(self) -> str:
        nodes = []
        current = self.head
        while current:
            if current == self.head:
                nodes.append("[Head {}]".format(current.data))
            elif current.next_node == None:
                nodes.append("[Tail {}]".format(current.data))
            else:
                nodes.append("[{}]".format(current.data))
            current = current.next_node
        return '->'.join(nodes)

if __name__ == "__main__":
    N1 = Node(10)
    N2 = Node(20)
    N1.next_node = N2
    print(N1, N1.next_node)
    
    l = linked_list()
    l.head = N1
    l.add(0) # prepend Node
    l.insert(5,1)
    print(l)
    l.remove(1)
    print(l)
    # print(l.search(10))