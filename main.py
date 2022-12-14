from rendering import convert_number_to_power


class Polynomial:

    def __int__(self):
        self.terms = []

    @classmethod
    def from_monomials(cls, terms):
        pass


class Monomial:

    def __init__(self, name, coefficient=1, power=1):
        self.name = name
        self.coefficient = coefficient
        self.power = power

    def __mul__(self, other):
        new_coefficient, new_power = self.coefficient, self.power
        if type(other) == int:
            new_coefficient = other * self.coefficient
        elif type(other) == Monomial:
            if other.name == self.name:
                new_coefficient = self.coefficient * other.coefficient
                new_power = self.power + other.power
            else:
                return Polynomial.from_monomials(self, other)
        else:
            raise ValueError("Can only multiply Monomial by int or Monomial, not by  " +str(type(other)))
        return Monomial(self.name, new_coefficient, new_power)

    def __rmul__(self, other):
        if type(other) == Monomial:
            return self
        return self.__mul__(other)

    def __imul__(self, other):
        new = self.__mul__(other)
        if type(new) == Polynomial:
            raise TypeError("Unsupported operand type *= for different monomials.'")
        self.coefficient = new.coefficient
        self.power = new.power
        return self

    def __truediv__(self, other):
        new_coefficient, new_power = self.coefficient, self.power
        if type(other) == int:
            new_coefficient = other / self.coefficient
        elif type(other) == Monomial:
            if other.name == self.name:
                new_coefficient = self.coefficient / other.coefficient
                new_power = self.power - other.power
            else:
                return Polynomial.from_monomials(self, other)
        else:
            raise ValueError("Can only multiply Monomial by int or Monomial, not by  " +str(type(other)))
        return Monomial(self.name, new_coefficient, new_power)

    def __rtruediv__(self, other):
        if type(other) == Monomial:
            return self
        return self.__truediv__(other)

    def __itruediv__(self, other):
        new = self.__truediv__(other)
        if type(new) == Polynomial:
            raise TypeError("Unsupported operand type /= for different monomials.'")
        self.coefficient = new.coefficient
        self.power = new.power
        return self

    def __mul__(self, other):
        new_coefficient, new_power = self.coefficient, self.power
        if type(other) == int:
            new_coefficient = other * self.coefficient
        elif type(other) == Monomial:
            if other.name == self.name:
                new_coefficient = self.coefficient * other.coefficient
                new_power = self.power + other.power
            else:
                return Polynomial.from_monomials(self, other)
        else:
            raise ValueError("Can only multiply Monomial by int or Monomial, not by  " +str(type(other)))
        return Monomial(self.name, new_coefficient, new_power)

    def __rmul__(self, other):
        if type(other) == Monomial:
            return self
        return self.__mul__(other)

    def __imul__(self, other):
        new = self.__mul__(other)
        if type(new) == Polynomial:
            raise TypeError("Unsupported operand type *= for different monomials.'")
        self.coefficient = new.coefficient
        self.power = new.power
        return self

    def __mul__(self, other):
        new_coefficient, new_power = self.coefficient, self.power
        if type(other) == int:
            new_coefficient = other * self.coefficient
        elif type(other) == Monomial:
            if other.name == self.name:
                new_coefficient = self.coefficient * other.coefficient
                new_power = self.power + other.power
            else:
                return Polynomial.from_monomials(self, other)
        else:
            raise ValueError("Can only multiply Monomial by int or Monomial, not by  " +str(type(other)))
        return Monomial(self.name, new_coefficient, new_power)

    def __rmul__(self, other):
        if type(other) == Monomial:
            return self
        return self.__mul__(other)

    def __imul__(self, other):
        new = self.__mul__(other)
        if type(new) == Polynomial:
            raise TypeError("Unsupported operand type *= for different monomials.'")
        self.coefficient = new.coefficient
        self.power = new.power
        return self

    def __str__(self):
        if self.coefficient == 0:
            return "0"
        return f"{self.coefficient if self.coefficient != 1 else ''}{self.name}{convert_number_to_power(self.power)}"
    __repr__ = __str__


def var(name):
    return Monomial(name)


x = var("x")
print(x)
x *= 3
print(x)
print(4*x*x)
