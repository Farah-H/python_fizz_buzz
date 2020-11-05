# creating a class for the FizzBuzz function

class FizzBuzz():

    def __init__(self, fizz, buzz, start, end): # initialising the class to take 4 inputs
        self.fizz = fizz
        self.buzz = buzz
        self.start = start 
        self.end = end

    def check_numbers(self):
        numbers = [] # empty list which we can appent numbers or fizz / buzz to 
        # i think this is better than a list of 1-100 which we then go and replace elements of

        # control flow to check divisibility
        for number in range (self.start, self.end + 1):
            if number % self.buzz == 0 and number % self.fizz == 0:
                numbers.append('FizzBuzz') 
            elif number % self.buzz == 0:
                numbers.append('Buzz')
            elif number % self.fizz == 0:
                numbers.append('Fizz')
            else:
                numbers.append(number)
        return number
        



fizz = int(input('What number would you like to replace multiples of with "Fizz"?'))
buzz = int(input('What number would you like to replace multiples of with "Buzz"?'))
start = int(input('Where would you like to start?'))
end = int(input('Where would you like to end?'))

if start != 0:
    test = FizzBuzz(fizz, buzz, start, end)
    print(test.check_numbers())
else:
    print('Please enter a non-zero integer.')
