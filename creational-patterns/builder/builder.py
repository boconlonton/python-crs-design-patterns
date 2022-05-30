"""
Implement the builder patterns

USE WHEN: object creation requires too many steps

"""


class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.text = text
        self.name = name
        self.elements = []

    def _to_string(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' + ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent+1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self._to_string(0)

    # @staticmethod
    # def create(name):
    #     return Html


class HtmlBuilder:
    _root = HtmlElement()

    def __init__(self, root_name):
        self.root_name = root_name
        self._root.name = root_name

    # not fluent
    def add_child(self, child_name, child_text):
        self._root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def __str__(self):
        return str(self._root)


root = HtmlBuilder('ul')
root.add_child()
