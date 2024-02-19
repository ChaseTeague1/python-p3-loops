#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i in range(10, 0, -1):
        print(f"{i}")
        i -= 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    int_list = [integer ** 2 for integer in int_list]
    return int_list
    pass

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5: 
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)
    pass
