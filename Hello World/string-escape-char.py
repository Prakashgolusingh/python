#=========================Lecture-17(String)=======================
greeting = "Hello"
# taking input from user by default it's string type
# you have to change data type for integer, decimal , etc.
name = "Krishna" 
print ( greeting + name )
print ( greeting + " " + name )

# output --:
'''
HelloKrishna
Hello Krishna
'''

#===================Lecture-18(Escape)=================================
SplitString = "This string has been \nsplit over \nseveral\nlines"
# after backslash we use any character to do some special task
# eg. 'n' use for new line, 't' use for space of length tab
print(SplitString)
print("1\t2\t3\t4\t5") # this create tab space between nos.
# a string with single quote we use escape char. to insert single quote.
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
# Inside double quote we  can easily use single quote and vice-versa
# in string of double quote we use escape char to add double quote
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

#OR
# We can use three double quote for string in python
print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")
#or
# similarly we can use three single quote for string.
print('''The pet shop owner said "No, no, 'e's uh,...he's resting".''')


#! Strng in three single/double quote print the string as its structure
str = '''This string has been
split over
several
lines'''
print(str)
# using backslash(\)end of string in three quote don't allow string to break in several line
str = '''This string has been \
split over \
several \
lines'''
print(str)
# or
print("""This string has been
split over
several
lines""")

# output--:
'''
This string has been 
split over 
several
lines
1	2	3	4	5
The pet shop owner said "No, no, 'e's uh,...he's resting".
The pet shop owner said "No, no, 'e's uh,...he's resting".
The pet shop owner said "No, no, 'e's uh,...he's resting".
The pet shop owner said "No, no, 'e's uh,...he's resting".
This string has been
split over
several
lines
This string has been split over several lines
This string has been
split over
several
lines
'''



