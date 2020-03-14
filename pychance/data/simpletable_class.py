import random


class SimpleTable:
    def __init__(self, table_name, table_values = None):
        self.table_name = table_name

        if table_values is not None:
            if isinstance(table_values, list):
                self.table_values = table_values
            else:
                self.table_values = []
        else:
            self.table_values = []

    def add_value(self, table_value):
        self.table_values.append(table_value)

    def get_value(self):
        random.shuffle(self.table_values)
        return self.table_values[0]


if __name__ == '__main__':
    test = SimpleTable("foo", ["bar", "baz"])
    print(test.get_value())
