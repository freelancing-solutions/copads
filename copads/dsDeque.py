"""
https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaDequeinPython.html
"""
class Deque:
    def __init__(self):
        self.items: list = []

    def is_empty(self) -> bool:
        return self.items == []

    def add_front(self, item: any) -> None:
        self.items.append(item)

    def add_rear(self, item: any) -> None:
        self.items.insert(0, item)

    def remove_front(self) -> any:
        return self.items.pop()

    def remove_rear(self) -> any:
        return self.items.pop(0)

    def size(self) -> int:
        return len(self.items)
