# Python OOP Task - FizzBuzz

## Task 
__Core:__
Write a program that prints the numbers from 1 to 100. For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz" instead of the number For numbers which are multiples of both three and five print "FizzBuzz".

__Extra:__
Make a new fizzbuzz file and make it functional make it so we we can decide which numbers to substitute for fizz and buzz using functions

## Pre-Requisites
__Necessary:__ You must have python installed.  
__Optional:__ It is easier to complete this task when using a code editor, such as Visual Studio Code or PyCharm. You can learn how to [install VSC](https://docs.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2019) or [install PyCharm](https://www.jetbrains.com/help/pycharm/quick-start-guide.html) using these hyperlinks. 

## Syntax 
### Step 1: Creating and Initialising a FizzBuzz class 
```python
class FizzBuzz():
    # initialising the class to take 4 inputs
    def __init__(self, fizz, buzz, start, end):    
        self.fizz = fizz
        self.buzz = buzz
        self.start = start 
        self.end = end
```
### Step 2: Control Flow to Check Divisibility
__Please note the indentation, this block is contained within the class__

```python
    def check_numbers(self):
        numbers = [] 
        # empty list which we can appent numbers or fizz / buzz to 
        # I think this is better (and easier) than a list of 1-100 which we then go and replace elements of

        # control flow to check divisibility and append either Fizz, Buzz, FizzBuzz or the number to a list
        for number in range (self.start, self.end + 1):
            if number % self.buzz == 0 and number % self.fizz == 0:
                numbers.append('FizzBuzz') 
            elif number % self.buzz == 0:
                numbers.append('Buzz')
            elif number % self.fizz == 0:
                numbers.append('Fizz')
            else:
                numbers.append(number)
        return ' '.join(str(number) for number in numbers) 
        # this returns a string seperated by a space (makes the output pretty without square brackets)
```

### Step 3: In a Seperate File, Run the Function and Prompt User for Inputs
__You must make sure to import the classs using the filename you saved it as__
```python
# importing the class
from fizz_buzz_class import FizzBuzz
```
Recalling that when we initialised the class we specified that it must take 4 inputs: `start, end, fizz, buzz` we prompt the user for these:
```python
# promting the user for inputs
fizz = int(input('What number would you like to replace multiples of with "Fizz"?'))
buzz = int(input('What number would you like to replace multiples of with "Buzz"?'))
start = int(input('Where would you like to start?'))
end = int(input('Where would you like to end?'))
```

### Step 4: Run the Class Method by Instantiating the Class
__Here I also checked that the range does not contain 0, as this creates issues since the modulus of 0 / anything = 0 and anything / 0 yields infinity.__

```python
# return an error if 0 is in the range, otherwise run
if 0 not in (range(start, end), fizz, buzz):
    # creating an instance of the class
    fizz_buzz_instance = FizzBuzz(fizz, buzz, start, end)
    print(fizz_buzz_instance.check_numbers()) # runs FizzBuzz function
else:
    print('0 cannot be in the range of start, end nor can it be Fizz or Buzz, please try another input.')
```