
class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current % 2 == 0:
            if self.current < self.end:
                result = self.current
                self.current += 2
                return result
            else:
                raise StopIteration


en = EvenNumbers(10, 25)
for i in en:
    print(i)
