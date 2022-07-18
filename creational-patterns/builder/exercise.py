"""
Builder Coding Exercise:
- You are asked to implement the Builder design pattern for rendering simple
chunks of code.
- Sample use of the builder you are asked to create:
cb = CodeBuilder('Person').add_field('name', '""')
                            .add_field('age', '0')
print(cb)
"""


class CodeBuilder:
    def __init__(self, root_name):
        # TODO
        self.root_name = root_name
        self._fields = []

    def add_field(self, _type, name):
        # TODO
        self._fields.append((_type, name))
        return self

    def __str__(self):
        # TODO
        if self._fields:
            init_str = "".join(
                "    self." + _type + " = " + str(name) + "\n"
                for _type, name in self._fields
            )
            return 'class ' + self.root_name + ':\n' +\
                   '  def __init__(self):\n' + \
                   init_str
        else:
            return 'class ' + self.root_name + ':\n' + '  pass'


cb = CodeBuilder('Person')\
    .add_field('name', '""')\
    .add_field('age', '0')
print(cb)
