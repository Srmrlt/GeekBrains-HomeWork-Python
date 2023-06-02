class Stationery:

    def __init__(self, title):
        self.title = title
        print(self.title)

    @staticmethod
    def draw():
        print('start')


class Pen(Stationery):

    @staticmethod
    def draw():
        print('pen')


st = Stationery('r')
st.draw()
pen = Pen('e')
pen.draw()
