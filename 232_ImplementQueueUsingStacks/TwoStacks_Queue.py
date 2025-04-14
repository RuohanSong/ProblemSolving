# time complexity: O(1)

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []


    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if self.empty():
            print("Queue is empty")
            return
        else:
            self.peek()
            return self.s2.pop()

    def peek(self) -> int:
        if self.empty():
            print("Queue is empty")
            return
        elif not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2[-1]
        else:
            return self.s2[-1]


    def empty(self) -> bool:
        return not self.s1 and not self.s2


# Your MyQueue object will be instantiated and called as such:
q = MyQueue()
q.push(1)   # s1 = [1]
q.push(2)   # s1 = [1, 2]
q.push(3)   # s1 = [1, 2, 3]
print("s1=", q.s1)
print("s2=", q.s2)
print(q.peek())

# Now do a pop → transfers s1 to s2
q.pop()     # s1 = [], s2 = [3, 2] (1 was popped)
print("s1=", q.s1)
print("s2=", q.s2)
print(q.peek())

# Push new values
q.push(4)   # s1 = [4]
q.push(5)   # s1 = [4, 5]
print("s1=", q.s1)
print("s2=", q.s2)
print(q.peek())

q.pop()     # 2 was popped
q.pop()
print("s1=", q.s1)
print("s2=", q.s2)
print(q.peek())
print("s1=", q.s1)
print("s2=", q.s2)