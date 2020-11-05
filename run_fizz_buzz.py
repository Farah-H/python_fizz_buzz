from fizz_buzz_class import FizzBuzz

fizz = int(input('What number would you like to replace multiples of with "Fizz"?'))
buzz = int(input('What number would you like to replace multiples of with "Buzz"?'))
start = int(input('Where would you like to start?'))
end = int(input('Where would you like to end?'))

if start != 0:
    test = FizzBuzz(fizz, buzz, start, end)
    print(test.check_numbers())
else:
    print('Please enter a non-zero integer.')