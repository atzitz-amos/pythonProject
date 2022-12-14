

class Polynomial:

    def __int__(self):
        self.terms = []

    @classmethod
    def from_monomial(cls, monomial):
        pass


class Monomial:

    def __init__(self, name, coefficient):
        self.name = name
        self.coefficient = coefficient


def var(name):
    return Monomial(name)
