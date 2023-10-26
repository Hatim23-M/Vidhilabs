for i in range(1, 101):
    if i%21==0:
        print("FizzBuzz")
    elif i%7==0:
        print("Fizz")
    elif i%3==0:
        print("Buzz")
    else:
        print(i)