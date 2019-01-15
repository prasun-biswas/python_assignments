class Fraction:
    """ This class represents one single fraction that consists of
        numerator and denominator """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: fraction's numerator
        :param denominator: fraction's denominator
        """

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator
        self.num = numerator
        self.denom = denominator

    def return_string(self):
        """ Returns a string-presentation of the fraction in the format
        numerator/denominator """

        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return "{:s}{:d}/{:d}".format(sign, abs(self.__numerator),
                                     abs(self.__denominator))

    def simplify(self):
        gcd = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator//gcd
        self.__denominator = self.__denominator//gcd

    def reciprocal(self):
        #self.__denominator = -1 * self.__denominator
        #self.__numerator = -1 * self.__numerator
        return  Fraction(self.__denominator, self.__numerator)

    def complement(self):
        num = self.__numerator
        denom = self.__denominator
        if num*denom<0:
            denom = -1 * denom
        else:
            denom = -1 * denom
        #self.__numerator = -1 * self.__numerator
        return Fraction(num, denom)

    def multiply(self, other):
        num = self.__numerator
        dinom = self.__denominator
        n = other.num
        d = other.denom

        return Fraction(num*n, dinom*d)

    def divide(self, other):
        num = self.__numerator
        dinom = self.__denominator
        n = other.num
        d = other.denom

        return Fraction(num*d, dinom*n)

    def add(self,other):
        num = self.__numerator
        dinom = self.__denominator
        n = other.num
        d = other.denom

        return Fraction((num * d + dinom*n), dinom * d)

    def deduct(self,other):
        num = self.__numerator
        dinom = self.__denominator
        n = other.num
        d = other.denom

        return Fraction((num * d - dinom * n), dinom * d)

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """

    while b != 0:
        a, b = b, a % b
    return a

def main():
    while True:
        command = input("> ")
        if command == "add":
            user_input = input("Enter a fraction in the form integer/integer: ")
            second_input = input("Enter a name: ")
        elif command == "quit":
            print("Bye bye!")
            break
        else:
            print("Unknown command!")


main()