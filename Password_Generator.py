#Jacob Case - July 6, 2021
#password generator script in python
#ask user for input on length
#ask user for digits?
#ask user for letters?
#ask user for input on special characters?
#ask user to store password in log with comments

#imports
import random
import string
from datetime import datetime

#Welcome messages
print("Welcome to Password Generator program.")
print("Program takes in two arguments and generates a relative password.")
print("Once password has been generated, user can write a comment with generated password and save in logfile.")
print (datetime.now())

#User Inputs
l = input ("Please enter desired password length: ")
asc_input = input ("Include alpha characters (y or n)? ")
dig_input = input ("include 0-9 digits (y or n) ?")
sc_input  = input ("Include special characters (y or n)? ")

#increment random seed

random.seed(datetime.now())

#functions
def get_ascii(length):
    mypw = ""
    for x in range(int(length)):
        mypw += random.choice(string.ascii_letters)
    return mypw;

def get_digit(length):
    mypw = ""
    for x in range(int(length)):
        mypw += random.choice(string.digits)
    return mypw;

def get_special(length):
    mypw = ""
    for x in range(int(length)):
        mypw += random.choice(string.punctuation)
    return mypw;

def get_ascii_digit(length):
    mypw = ""
    for x in range(int(length)):
        mypw += random.choice(string.ascii_letters + string.digits)
    return mypw;

def get_ascii_dig_special(length):
    mypw = ""
    for x in range(int(length)):
        mypw += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return mypw;

def get_ascii_special(length):
    mypw = ""
    for x in range(int(length)):
        mypw += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return mypw;

def get_digit_special(length):
    mypw = ""
    for x in range(int(length)):
        mypw += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return mypw;

if asc_input == "y" and dig_input == "n" and sc_input == "n":
    pw = get_ascii_dig_sc(l)
    print(pw)
elif asc_input == "n" and dig_input == "y" and sc_input == "n":
    pw = get_digit(l)
    print(pw)
elif asc_input == "n" and dig_input == "n" and sc_input == "y":
    pw = get_special(l)
    print(pw)
elif asc_input == "y" and dig_input == "y" and sc_input == "n":
    pw = get_ascii_digit(l)
    print(pw)
elif asc_input == "y" and dig_input == "n" and sc_input == "y":
    pw = get_ascii_special(l)
    print(pw)
elif asc_input == "n" and dig_input == "y" and sc_input == "y":
    pw = get_digit_special(l)
    print(pw)
elif asc_input == "y" and dig_input == "y" and sc_input == "y":
    pw = get_ascii_special(l)
    print(pw)
