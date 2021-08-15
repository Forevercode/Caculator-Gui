from ec import ErroeMessageToUser,InValidNumberError
from copy import deepcopy
import re

class Number:
    def get_number(str_expression, operator_index):
        str_expression = str_expression
        first_number = []
        second_number = []
        where_the_first_number_start = int(operator_index)
        where_the_second_number_end = int(operator_index)

        # grab_first_number
        str_expression_copy = list((str_expression[0:operator_index]))
        str_expression_copy.reverse()
        for i in str_expression_copy:
            if i not in ["+", "-", "×", "÷"]:
                first_number.insert(0, i)
            elif i in ["+", "-", "×", "÷"]:
                break
            where_the_first_number_start -= 1


        # grab_second_number
        for i in str_expression[operator_index + 1:len(str_expression)]:
            if i not in ["+", "-", "×", "÷"]:
                second_number.append(i)
            elif i in ["+", "-", "×", "÷"]:
                break
            where_the_second_number_end += 1

        first_number_str = "".join(first_number)
        second_number_str = "".join(second_number)

        #
        try:
            # check if there is any  number having dot at first or last position
            if re.match("^\.|\.$", first_number_str)!= None or re.match("^\.|\.$",second_number_str)!= None:
                raise InValidNumberError

            first_number_pack=[float(first_number_str) , where_the_first_number_start]
            second_number_pack=[float(second_number_str), where_the_second_number_end]
            return [first_number_pack,second_number_pack]

        except ValueError:#this prblom happen when there is  nothing before or after  an operator
            pass
        except InValidNumberError:#this prblom happen when there is any number having dot at first or last position
            pass



    def str_expression_calculate(str_expression):

        try:
            str_expression = str_expression
            for i in str_expression:
                if i == "×"  or i=="*" or i == "÷" or i=="/":

                    if i == "÷" or i=="/":
                        first_number_pack, second_number_pack = Number.get_number(str_expression=str_expression, operator_index=str_expression.index(i))
                        result = first_number_pack[0] / second_number_pack[0]
                        str_expression = str_expression[:first_number_pack[1]] + str(result) + str_expression[
                                                                                               second_number_pack[
                                                                                                   1] + 1:]
                    elif i == "×" or "*":

                        first_number_pack,second_number_pack=Number.get_number(str_expression=str_expression,operator_index=str_expression.index(i))
                        result = first_number_pack[0] * second_number_pack[0]

                        str_expression = str_expression[:first_number_pack[1]] + str(result) + str_expression[ second_number_pack[1] + 1:]




            for i in str_expression:
                if i == "+" or i == "-":
                    if i == "+":
                        first_number_pack,second_number_pack=Number.get_number(str_expression=str_expression,  operator_index=str_expression.index(i))
                        result = first_number_pack[0] + second_number_pack[0]
                        str_expression = str_expression[:first_number_pack[1]] + str(result) + str_expression[second_number_pack[1] + 1:]


                    elif i == "-":
                        first_number_pack,second_number_pack=Number.get_number(str_expression=str_expression,operator_index=str_expression.index(i))
                        result = first_number_pack[0] - second_number_pack[0]

                        str_expression = str_expression[:first_number_pack[1]] + str(result) + str_expression[ second_number_pack[ 1] + 1:]


            #return inttype if str_expression is interger(1there is dot in the value,no vlaue after the dot )
            if  str_expression.find(".")>0 and int((str_expression[str_expression.find(".")+1:]))==0  :
                return int(float(str_expression))
            else:
                return (str_expression)

        # this problem happen when there is some operators without having numbers at both front and back
        # and the 'get_number_fuction' return nothing
        except TypeError:
            return ErroeMessageToUser.bad_expression


    def only_demical_in_expression(str_expressipn):
        #maketrans return new string
        no=""
        operator_or_dot="+-×÷.*/"

        table=str_expressipn.maketrans(no,no,operator_or_dot)
        str_expressipn=str_expressipn.translate(table)
        return str_expressipn.isdecimal()

    def fist_and_last_number_is_not_invalid_number(str_expressipn):
        print(re.match("\.$",str_expressipn))
        if not re.match("^\.",str_expressipn) and not re.match("\.$",str_expressipn):
            return True
        return False

