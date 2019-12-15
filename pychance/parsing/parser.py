import re


class Parser:
    def __init__(self, pychance_instance):
        self.pychance_instance = pychance_instance
        self.simple_list_pattern = re.compile(r"(\[(?P<list>[a-zA-Z_][a-zA-Z0-9_]+?)\])")

    def parse(self, message):
        match = self.simple_list_pattern.search(message)
        while match is not None:
            which_list = match.group('list')

            if which_list in self.pychance_instance.tables:
                message = self.simple_list_pattern.sub(self.pychance_instance.tables[which_list].get_value(), message)
            else:
                message = self.simple_list_pattern.sub('undefined', message)

            match = self.simple_list_pattern.search(message)

        return message
