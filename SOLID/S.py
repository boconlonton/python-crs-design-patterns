# SRP - Single Responsibility
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # Break the SRP
    # def save(self, filename):
    #     pass
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        pass

j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug')
print(f'Journal entries:\n{j}')
