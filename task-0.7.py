def convert_farheineit(c):
    f = (9/5 * c) + 32
    print("Farheineit: " + str(f))

def convert_celsius(f):
    c = (5/9) * ((32 * f) - 32)
    print("Celsius: " + str(c))


convert_farheineit(0)
convert_celsius(0)
