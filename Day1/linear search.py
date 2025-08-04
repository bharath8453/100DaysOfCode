class LinearSearch:
    def __init__(self, vals):
        self.vals = vals

    def search(self, target):
        for i in range(len(self.vals)):
            if self.vals[i] == target:
                print(f"Element {target} found at index {i}")
                return i
        print(f"Element {target} not found")
        return -1


# Example Usage
ls = LinearSearch([10, 20, 30, 40])
ls.search(30)
ls.search(100)
