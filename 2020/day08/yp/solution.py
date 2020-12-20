with open('input.txt') as f:
    data = [line for line in f]


class BootCode:
    def __init__(self):
        self.data = data
        self._init()
    
    def _init(self, magic=1):
        self.accumulator = 0
        self._index = 0
        self._history = set()
        self._secret = 1
        self._magic_num = magic
    
    def run(self, retry=False):
        while self._index not in self._history:
            self._history.add(self._index)
            try:
                op, value = self.data[self._index].split()
                getattr(self, op)(value)
            except IndexError:
                return self.accumulator
        if retry:
            self._init(magic=self._magic_num + 1)
            return self.run(retry=True)
        else:
            return self.accumulator

    def acc(self, value):
        if value[0] == '+':
            self.accumulator += int(value[1:])
        else:
            self.accumulator -= int(value[1:])
        self._index += 1

    def nop(self, value, incr=True):
        if self._secret == self._magic_num:
            self._secret += 1
            return self.jmp(value, False)
        self._index += 1
        if incr:
            self._secret += 1

    def jmp(self, value, incr=True):
        if self._secret == self._magic_num:
            self._secret += 1
            return self.nop(value, False)
        if value[0] =='+':
            self._index += int(value[1:])
        else:
            self._index -= int(value[1:])
        if incr:
            self._secret += 1


klass = BootCode()
print(klass.run(retry=True))
print(klass._history)