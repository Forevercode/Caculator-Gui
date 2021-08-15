unsolved:
     0.2*7=1.400...001
     use regex to check if a number is integer



type--
   1.(get_number)
     return float anyway

   2.(str_expression_calculate)
     -1.it calculate any numbers with type float
     -2 if integer :return inttype
        if not integer :return stringtype

   3.(button_equal)
      don't do anything



invalid input filter--
   1.(button_equal)
    expression is allowed to include[+-×*÷/.0-9] only

   2(get_number)
     -1 there is  nothing before or after some  operators
     -2 the first number or second number is like (.2)

bad expression--
    (button equal)

    (str_expression_calculate)-<nothing return from(get_nember)>
                                 <-1 there is  nothing before or after some  operators>
                                 <-2 the first number or second number is like (.2)>