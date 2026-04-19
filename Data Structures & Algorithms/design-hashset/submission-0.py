class MyHashSet:

    def __init__(self):
        self.mapping = {}

    def add(self, key: int) -> None:
        self.mapping[key] = self.mapping.get(key, 0) + 1

    def remove(self, key: int) -> None:
        if key in self.mapping:
            self.mapping.pop(key)

    def contains(self, key: int) -> bool:
        return key in self.mapping


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)