# coding: utf-8

print "Bienvenido"
escribe = int(raw_input("Escribe un número del 1 al 100: "))

for x in range(1, escribe+1):
    if x % 3 == 0 and x % 5 == 0:
        print "fizzbuzz"
    elif x % 3 == 0:
        print "fizz"
    elif x % 5 == 0:
        print "buzz"
    else:
        print x