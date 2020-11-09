# importing the class
from fizz_buzz_class import FizzBuzz


# promting the user for inputs
fizz = int(input('What number would you like to replace multiples of with "Fizz"?'))
buzz = int(input('What number would you like to replace multiples of with "Buzz"?'))
start = int(input('Where would you like to start?'))
end = int(input('Where would you like to end?'))

# return an error if 0 is in the range, otherwise run
if 0 not in (range(start, end), fizz, buzz):
    # creating an instance of the class
    fizz_buzz_instance = FizzBuzz(fizz, buzz, start, end)
    print(fizz_buzz_instance.check_numbers()) # runs FizzBuzz function
else:
    print('0 cannot be in the range of start, end nor can it be Fizz or Buzz, please try another input.')