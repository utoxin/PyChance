from pychance.parsing import Parser


class PyChance:
    def __init__(self):
        self.tables = {}
        self.parser = Parser(self)

    def add_table(self, name, table):
        self.tables[name] = table


if __name__ == '__main__':
    from pychance import data
    test_table = data.SimpleTable("foo", ["bar", "baz"])

    test = PyChance()
    test.add_table("foo", test_table)
    print(test.parser.parse("This is a [foo] test."))

