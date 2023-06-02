class Worker:
    name = 'Karl'
    surname = 'Gib'
    position = 'tester'
    _income = {'wage': 10, 'bonus': 2}


class Position(Worker):

    @staticmethod
    def get_full_name():
        return Position.name + ' ' + Position.surname

    @staticmethod
    def get_total_income():
        return Position._income.get('wage') + Position._income.get('bonus')


pos = Position()
print(pos.get_full_name())
print(pos.get_total_income())
