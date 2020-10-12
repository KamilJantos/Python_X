
class OctalFormatterObs:
    def notify(self, publisher):
        value = oct(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now octal data = {value}")
