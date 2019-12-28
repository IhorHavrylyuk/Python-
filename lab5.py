"""SOLID
    S - single responsibilities
    O - open / closed
    L - Liskov
    I - interface segregation
    D - dependancy inversion
    Тут я відтворив принцип S так : у мене є 4 класи, кожен з яких має
    розподілені умови: 1 створює фігуру, 2 малює її, 3 s 4 проводять геометричні обрахунки.
    Принцип О - тут він відображений наприклад у тому, що для малювання фігури, нам
    не потрібно перевіряти тип фігури і під неї писати формулу малювання. Тут кожен клас фігури
    сам відповідає за свою формулу.
    Принцип L - пов'язаний з принципом O, ми можемо доступатись до функцій класу drawFigure об'єкти
    класів DrawTriangle та DrawSphere
    Принцип I - класу Трикутник не потрібно реалізовувати функцію пошуку об'єму.
    Принцип D - усі класи, і Трикутник , і Сфера залежать від абстракцій а
    не від конкретних реалізацій
    """


class Figure:
    def getPosition(self):
        pass

    def setPosition(self, *args):
        pass


class Figure2DGeometry:
    def calcS(self):
        pass

    def calcP(self):
        pass


class Figure3DGeometry:
    def calcV(self):
        pass


class DrawFigure:
    def draw(self):
        pass

#####################################################

class Triangle:
    A = B = C = (0, 0)

    def setPosition(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c

    def getPosition(self):
        print("Three points -- {0} , {1}, {2}".format(self.A, self.B, self.C))


class TriangleGeometry:
    def __init__(self, triangle):
        self.triangle = triangle

    def calcS(self):
        pass    # do some math

    def caclP(self):
        pass    # do some math


class TriangleDraw:
    def __init__(self, triangle):
        self.triangle = triangle

    def draw(self):
        if self.triangle:
            print('I`m a triangle')


class Sphere:
    center = (0, 0)
    radius = 0

    def setPosition(self, c, r):
        self.center = c
        self.radius = r

    def getPosition(self):
        print("Center -- {0} and radius -- {1}".format(self.center, self.radius))


class SphereGeometry:
    def __init__(self, sphere):
        self.sphere = sphere

    def calcV(self):
        pass  # do some math


class SphereDraw:
    def __init__(self, sphere):
        self.sphere = sphere

    def draw(self):
        if self.sphere:
            print('I`m a sphere!')


if __name__ == '__main__':
    fig1 = Triangle()
    fig2 = Triangle()
    fig3 = Sphere()
    fig1_draw = TriangleDraw(fig1)
    fig2_draw = TriangleDraw(fig2)
    fig3_draw = SphereDraw(fig3)
    lst = [fig1_draw, fig2_draw, fig3_draw]
    for i in lst:
        i.draw()