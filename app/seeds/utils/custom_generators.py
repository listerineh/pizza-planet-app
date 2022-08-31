from flask_seeder import generator

names_file = 'app/seeds/data/names.txt'
domains_file = 'app/seeds/data/domains.txt'


class PriceGenerator(generator.Generator):

    def __init__(self, initial: int = 1, final: int = 10, **kwargs):
        super().__init__(**kwargs)
        self._initial = initial
        self._final = final

    def generate(self):
        return round(self.rnd.uniform(self._initial, self._final), 2)


class ListGenerator(generator.Generator):
    def __init__(self, data: list, **kwargs):
        super().__init__(**kwargs)

        self._data = data
        self._start = 0
        self.end = len(self._data)

        self._next = self.start

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value
        if self._next < self._start:
            self._next = self._start

    def generate(self):
        value = self._next
        self._next += 1

        return self._data[value]
