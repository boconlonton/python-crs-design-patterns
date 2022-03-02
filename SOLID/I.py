# ISP - Interface Segregation Principal
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError
    
    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MutiFunctionPrinter(Machine):
    def print(self, document):
        pass
    
    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashinedPrinter(Machine):
    def print(self, document):
        # ok
        pass
    
    def fax(self, document):
        pass

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError("Printer cannot scan!")


# Conform the ISP Principal
class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner) -> None:
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
