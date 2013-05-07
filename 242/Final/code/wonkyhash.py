class WonkyHashTable():
    def __init__(self, size=4):
        self.table = [[] for i in range(size)]

    def add_element(self, element):
        self.table[self.bad_hash(element)] = element

    def contains(self, element):
        for t in self.table:
            if element in t:
                return True
        return False

    def bad_hash(self, element):
        return len(element) % len(self.table)

    def __str__(self):
        st = ""
        for t in self.table:
            st += str(t) + "\n"
        return st

htable = WonkyHashTable()
for elm in ['I', 'wrestled', 'a', 'bear', 'once']:
    htable.add_element(elm)
