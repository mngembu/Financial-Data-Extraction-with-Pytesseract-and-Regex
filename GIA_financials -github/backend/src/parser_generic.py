import abc  #for implementing abstract class to ensure each child class has atleast 1 mthod of its own


class AuditReportParser(metaclass=abc.ABCMeta):
    def __init__(self, text):
        self.text = text
# this class takes the balancesheet and income statement that we got from pytesseract as input and then
# uses the parse method below to return a json object or dict

    @abc.abstractmethod
    def parse(self):
        pass
