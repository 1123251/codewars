class SecureList:
    def __init__(self, lst):
        self.lst = lst

    def __getitem__(self, item):
        if len(self.lst) > 0:
            return self.lst.pop(item)
        else:
            return self.lst[item]

    def __repr__(self):
        test = self.lst
        while len(self.lst) != 0:
            self.lst.pop()
        return f"{test}"

    def __len__(self):
        return len(self.lst)


base = [13, 2, 3, 4]
a = SecureList(base)

print(a[0], base[0], "List returned wrong value.")
print(a[0], base[1], "List returned wrong value.")

