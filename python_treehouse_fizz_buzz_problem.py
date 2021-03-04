name = input("Please enter your name: ")
number = input("Please enter a number: ")

# prints name and number
print("Hello, {}".format(name))
print("The number you've selected is {}".format(number))


# checks to see if divisible by 3 aka "Fizz"
check_fizz = (int(number) % 3)

# checks to see if dibisible by 5 aka "buzz"    
check_buzz = (int(number) % 5) 

# checks if fizzbuzz, fiz, buzz, or neither
if check_fizz == 0 and check_buzz == 0:
  print("{} is a FizzBuzz number.".format(number))
  
elif check_fizz == 0:
    print("it's a fizz")

elif check_buzz == 0:
    print("it's a buzz")

else: 
  print("{} is neither a fizzy or a buzzy number.".format(number))
    
# TODO: Make sure the number is an integer


# TODO: Print out the User's name and the number entered,
# making sure the two statements are on separate lines of output.


# TODO: Compare the number the user gave with the different
# FizzBuzz conditions. 
# *********************
# If the number is divisible by 3, print "is a Fizz number."
# If the number is divisible by 5, print "is a Buzz number."
# If the number is divisible by both 3 and 5, print "is a FizzBuzz number."
# Otherwise, print "is neither a fizzy or a buzzy number."
# *********************


# TODO: Define variables for is_fizz and is_buzz that stores 
# a Boolean value of the condition. Remember that the modulo operator, %, 
# can be used to check if there is a remainder.


# Using the variables, check the condition of the value, and print the necessary
# string




















