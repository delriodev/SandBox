#Definition
my_int = 3
my_float = -3.45

print(''' 
                        Operators                : + - * /
                        Floor division (Quotient): // 
                        Exponent                 : **
                        Modulus (Remainder)      : % 

                        Conparaisons             : == != > < >= <=
''')
print("                        my_int            = " + str(my_int))
print("                        my_float          = " + str(my_float))
print("                        type(my_int)      = " + str(type(my_int)))
print("                        type(my_float)    = " + str(type(my_float)))
my_int += 1
print("     Absolute value   : abs(-3.4)         = " + str(abs(my_float)))
print("     Increment        : my_int += 1       = " + str(my_int + 1))
print("     Round            : round(-3.4)       = " + str(round(my_float)))
print("     Round            : round(-3.4, 1)    = " + str(round(my_float, 1)))
print("     Casting          : int('10')         = " + str('10'))

