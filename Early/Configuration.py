class Configuration:
    start: str = 'S'
    finish: str = ''   # contains a dot "." !!!
    i: int = 0

    def __init__(self, start: str, finish: str, i: int):
        assert finish.index('.') != -1
        self.start = start
        self.finish = finish
        self.i = i

    def __eq__(self, other):
        return self.start == other.start and self.finish == other.finish and self.i == other.i

    def __str__(self):
        return "{}: {} -> {}".format(self.i, self.start, self.finish)

    def __hash__(self):
        return hash(str(hash(self.start)) + str(hash(self.finish)) + str(hash(self.i)))
