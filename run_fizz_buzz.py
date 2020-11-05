from fizz_buzz_class import FizzBuzz

fizz = int(input('What number would you like to replace multiples of with "Fizz"?'))
buzz = int(input('What number would you like to replace multiples of with "Buzz"?'))
start = int(input('Where would you like to start?'))
end = int(input('Where would you like to end?'))

if 0 not in (start, end, fizz, buzz):
    test = FizzBuzz(fizz, buzz, start, end)
    print(test.check_numbers())
else:
    print('0 cannot be in the range of start, end nor can it be Fizz or Buzz, please try another input.')