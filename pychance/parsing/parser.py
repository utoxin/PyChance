import re


class Parser:
    def __init__(self, pychance_instance):
        self.pychance_instance = pychance_instance
        self.simple_list_pattern = re.compile(r"(\[(?P<list>[a-zA-Z_][a-zA-Z0-9_]+?)])")
        self.special_case_a = re.compile(r"{a}(?P<spacing>\s+)(?P<next>\S)")

    def parse(self, message):
        match = self.simple_list_pattern.search(message)
        while match is not None:
            which_list = match.group('list')

            if which_list in self.pychance_instance.tables:
                message = self.simple_list_pattern.sub(self.pychance_instance.tables[which_list].get_value(), message,
                                                       count=1)
            else:
                message = self.simple_list_pattern.sub('undefined', message, count=1)

            match = self.simple_list_pattern.search(message)

        match = self.special_case_a.search(message)
        while match is not None:
            next_letter = match.group('next')
            spacing = match.group('spacing')

            if next_letter in ['a', 'e', 'i', 'o', 'u']:
                message = self.special_case_a.sub(f"an{spacing}{next_letter}", message, count=1)
            else:
                message = self.special_case_a.sub(f"a{spacing}{next_letter}", message, count=1)

            match = self.special_case_a.search(message)

        return message
