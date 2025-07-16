class Node:
    def _init_(self,value):
        self.value = value
        self.next = None

class Queue:
    def _init_(self):
        self.front = None
        self.rear = None
        self.size = 0

#Have a dunder method length
    def _len_(self):
        return self.size
    #representationdunder
    def _repr_(self):
        items = []
        current_item = self.front
        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next

        return ', '.join(items)
    def enqueue(self,value):
        new_node = Node(value)
        #check if queue is empty
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
            #increase the size by one every time you enqueue
            self.size += 1
    def dequeue(self):
        #remove the front element if queue is not empty
        if self.front is None:#No front element thus raise an error
            raise IndexError('Queue is empty')
        dequeue_value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        self.size -=1
        return dequeue_value

    def peek(self):
        #check if queue is empty or not
        if self.front is None:
            raise IndexError('Queue is empty')
        return self.front.value
    def is_empty(self):
        return self.front is None
if __name__ == '_main_':
    q=Queue()
    q.enqueue(11)
    q.enqueue(22)
    q.enqueue(33)
    q.enqueue(44)
    q.enqueue(55)
    q.enqueue(66)
    print(q)
    print(len(q))
    print(q.dequeue())
    print(q.dequeue())
    print(q)
    print(len(q))