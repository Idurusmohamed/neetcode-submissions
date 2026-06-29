class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] # notice for this one how you actually have to return something and is not None.

    def getMin(self) -> int:
        tmp = []
        mini = self.stack[-1]

        while len(self.stack):
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())

        while len(tmp):
            self.stack.append(tmp.pop())
        
        return mini
