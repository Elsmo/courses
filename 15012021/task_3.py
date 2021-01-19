class Worker():
    def __init__(self, name, surname, position, income=None):
        if income is None:
            income = {"wage": 0, "bonus": 0}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self, total_income=0):
        for items in self._income:
            total_income += self._income[items]
        print(total_income)


bob = Position('Bob', 'Smit', 'operator', {"wage": 50000, "bonus": 5000})
bob.get_full_name()
bob.get_total_income()

ted = Position('Ted', 'Mosby', 'architector', {"wage": 80000, "bonus": 25000})
ted.get_full_name()
ted.get_total_income()
