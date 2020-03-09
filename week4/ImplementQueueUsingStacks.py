class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.left = []
        self.right = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.left.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        for _ in range(len(self.left) - 1):
            self.right.append(self.left.pop())
            
        out = self.left.pop()
        for _ in range(len(self.right)):
            self.left.append(self.right.pop())
        return out

    def peek(self) -> int:
        """
        Get the front element.
        """
        for _ in range(len(self.left) - 1):
            self.right.append(self.left.pop())
            
        out = self.left[0]
        for _ in range(len(self.right)):
            self.left.append(self.right.pop())
        return out

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.left) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()