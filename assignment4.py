print("QUESTION : 2 Write  a Python program to read an entire text file. ")
def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read('test.txt')

print("QUESTION : 3 Write a Python program to append text to a file and display the text. ")
def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("Python Exercises\n")
                myfile.write("Java Exercises")
        txt = open(fname)
        print(txt.read())
file_read('abc.txt')

print("QUESTION : 4 Write a Python program to read first n lines of a file. ")
f = open("myfile.txt","r")
a = f.readlines()
print(a)
f.close()

print("QUESTION : 5 Write a Python program to read last n lines of a file.") 
def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('test.txt',2)

print("QUESTION : 6 Write a Python program to read a file line by line and store it into a list")
with open("myfile.txt") as file:
    list = file.readlines()
    list = [list.rstrip() for list in list]
print(list)

print("QUESTION : 7 Write a Python program to read a file line by line store it into a variable.")
def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('test.txt')


print("QUESTION : 8 Write a python program to find the longest words.") 
word_list = ['apple','mango','papaya','ssdfghcvbncdvfbfghonm']

def find_longest_word(words):
    longest_word = ''
    for wdd in words: 
     if len(wdd) > len(longest_word):
      longest_word = wdd
print(' longest word is ' + find_longest_word)

find_longest_word(word_list)

print("QUESTION : 9 Write a Python program to count the number of lines in a text file.") 

print("QUESTION : 10 Write a Python program to count the frequency of words in a file. ")
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("example.txt"))




print("QUESTION : 11 Write a Python program to write a list to a file. ")
fruit_list = ['mango','kiwi','orange','chikoo','papaya','grapes']
print(fruit_list)
textfile = open ('/Users/lenovo/desktop/fruit_list','w')
content = '\n'.join(fruit_list)
textfile.writelines(content)



print("QUESTION : 12 Write a Python program to copy the contents of a file to another file.")
f1 = open("first.txt",mode='r')
f2 = open("second.txt",mode='w')
print(f1.readlines())
data = f1.readlines()
for line in f1:
    f2.written(line)
f1.close()
f2.close()

print("QUESTION : 20 Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle ")
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())
print("QUESTION : 21 Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle ")
print("QUESTION : 22 Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle")




"""

                            | MODULE 4 THEORY QUESTION |


QUE : 1] What is File function in python? What is keywords to create and write file?
ANS:
>> Python has a built-in open() function to open a file. This function returns a file object, also called a handle, as it is used to read or modify the file accordingly. We can specify the mode while opening a file. 

>>In mode, we specify whether we want to read r , write w or append a to the file.


QUE : 13] Explain Exception handling? What is an Error in Python?
ANS:
>> An Exception is an error that happens during the execution of a program. 

>> Whenever there is an error, Python generates an exception that could be handled. 

>> It basically prevents the program from getting crashed.



QUE : 14] How many except statements can a try-except block have? Name Some built-in exception classes: 
ANS:
>>  There has to be at least one except statement.

   >>         Exception	            |                             Description
     --------------------------------------------------------------------------------------------------------------------
        AttributeError	            |        Raised when attribute reference or assignment fails
         Exception	                |                Base class for all exceptions
         EOFError	                |                Raised when the input() method hits an "end of file" condition (EOF)
        FloatingPointError	        |                Raised when a floating point calculation fails



QUE :  15] When will the else part of try-except-else be executed?
ANS:
>> The else part is executed when no exception occurs.



QUE : 16] Can one block of except statements handle multiple exception? 
ANS:
>> In Python, try-except blocks can be used to catch and respond to one or multiple exceptions. 

>> In cases where a process raises more than one possible exception, they can all be handled using a single except clause



QUE : 17] When is the finally block executed? 
ANS:
>> The finally block always executes when the try block exits. 

>> This ensures that the finally block is executed even if an unexpected exception occurs.


QUE : 18] What happens when „1‟== 1 is executed? 
ANS: 
>> It simply evaluates to False and does not raise any exception.



QUE : 19] How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.
ANS:
>> Exception handling with try, except, else, and finally

>> Try: This block will test the excepted error to occur.

>> Except: Here you can handle the error.

>> Else: If there is no exception then this block will be executed.

>> Finally: Finally block always gets executed either exception is generated or not.



QUE : 21] What are oops concepts? Is multiple inheritance supported in java ?
ANS:
>> Multiple Inheritance is a feature of an object-oriented concept, where a class can inherit properties of more than one parent class. 

>> The problem occurs when there exist methods with the same signature in both the superclasses and subclass.



QUE  : 22] How to Define a Class in Python? What Is Self? Give An Example Of A Python Class
ANS:
>> A class creates a new local namespace where all its attributes are defined.

>> Attributes may be data or functions. There are also special attributes in it that begins with double underscores __ .

>>  For example, __doc__ gives us the docstring of that class.


QUE : 26] Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?
ANS:
>> 


QUE : 27] What is Instantiation in terms of OOP terminology?
ANS:
>> Instantiate (a verb) and instantiation (the noun) in computer science refer to the creation of an object (or an “instance” of a given class) in an object-oriented programming (OOP) language. 

>> Referencing a class declaration, an instantiated object is named and created, in memory or on disk


QUE : 28] What is used to check whether an object  is an instance of class A? 
ANS:
>> The isinstance() function checks if the object (first argument) is an instance or subclass of the class info class (second argument).


QUE : 29 What relationship is appropriate for Course and Faculty? 
ANS:
>> A department offers multiple courses ( Course objects), but in our implementation a course can only have a single department 
>> This is a one-to-many relationship.

QUE : 30 What relationship is appropriate for Student and Person?
ANS:
>> 
"""
