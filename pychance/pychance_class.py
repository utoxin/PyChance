from pychance.parsing import Parser


class PyChance:
    def __init__(self):
        self.tables = {}
        self.parser = Parser(self)

    def add_table(self, name, table):
        self.tables[name] = table


if __name__ == '__main__':
    from pychance.data import SimpleTable

    test_table = SimpleTable("foo", ["[bar]", "baz"])
    test_table2 = SimpleTable("bar", ["testing", "this"])

    test = PyChance()
    test.add_table("foo", test_table)
    test.add_table("bar", test_table2)
    print(test.parser.parse("This is a [foo] test [bar]."))

