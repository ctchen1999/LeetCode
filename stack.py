class Stack():
    def __init__(self) -> None:
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.items is None:
            return "Stack is empty."
        else:
            return self.items.pop()
    
    def peek(self):
        """
        See the topest element of the stack
        """
        if self.items is None:
            return "Stack is empty."
        else:
            return self.items[len(self.items) - 1]
    
    def __repr__(self) -> str:
        return ' -> '.join(self.items)
    
if __name__ == "__main__":
    s = Stack()
    c = 0
    while c != 4:
        print('\tSTACK OPERATIONS')
        print('1.Push')
        print('2.Pop')
        print('3.Peek')
        print('4.Exit')
        c = int(input('Enter your choice(1-5): '))
        if c == 1:
            x = input("Enter the item: ")
            s.push(x)
            print(s)
        elif c == 2:
            s.pop()
            print(s)
        elif c == 3:
            print(s.peek())
        elif c != 4:
            print('Wrong Choice! Choose from 1 to 5 only')

    print('Bye')