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

        divisor = greatest_common_divisor(self.__numerator,self.__denominator)
        self.__numerator = self.__numerator//divisor
        self.__denominator = self.__denominator//divisor


def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mul(num1,num2):
    num1_list = num1.split("/")
    num2_list = num2.split("/")
    res1 = int(num1_list[0])*int(num2_list[0])
    res2 = int(num1_list[1])*int(num2_list[1])
    res = str(res1)+"/"+str(res2)
    return res


def main():

    frac_dict = {}
    while True:
        command = input("> ")
        if command == "quit":
            print("Bye bye!")
            break
        elif command == "add":
            frac_num = input("Enter a fraction in the form integer/integer: ")
            name = input("Enter a name: ")
            if name not in frac_dict.keys():
                frac_dict[name] = frac_num

        elif command == "print":
            name = input("Enter a name: ")
            if name in frac_dict.keys():
                print(name,"=",frac_dict.get(name))
            else:
                print("Name", name, "was not found")

        elif command == "list":
            if len(frac_dict) == 0:
                continue
            else:
                for key, value in sorted(frac_dict.items()):
                    print(key,"=",value)

        elif command == "*":
            op_1 = input("1st operand: ")
            if op_1 in frac_dict.keys():
                op_2 = input("2nd operand: ")
                if op_2 in frac_dict.keys():
                    num1 = frac_dict.get(op_1)
                    num2 = frac_dict.get(op_2)
                    res = mul(num1,num2)
                    res_lst = res.split("/")
                    frac = Fraction(int(res_lst[0]),int(res_lst[1]))
                    print(num1,"*",num2,"=",frac.return_string())
                    frac.simplify()
                    print("simplified",frac.return_string())
                else:
                    print("Name", op_2, "was not found")
                    continue
            else:

                print("Name", op_1, "was not found")
                continue

        elif command == "file":
            filename = input("Enter the name of the file: ")
            try:
                file_obj = open(filename, "r")
                for line in file_obj:
                    row = line.rstrip().split("=")
                    name = row[0]
                    num = row[1]
                    num_lst = num.split("/")
                    if len(num_lst) != 2:
                        print("Error: the file cannot be read.")
                        break

                    frac_dict[name] = num
                file_obj.close()
            except IOError:
                print("Error: the file cannot be read.")
            except ValueError:
                print("Error: the file cannot be read.")
            except IndexError:
                print("Error: the file cannot be read.")
        else:
            print("Unknown command!")
            continue

main()
