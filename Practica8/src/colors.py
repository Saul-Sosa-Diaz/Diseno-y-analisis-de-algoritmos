"""
File: colors.py
Author: Saúl Sosa Díaz
Date: 27/03/2023
Description: This is a Python class definition named "bcolors". It defines several class variables, 
each of which is a string representing an ANSI escape code for changing the color or style of text displayed in a terminal. 
These escape codes can be used to customize the output of text in a terminal application, such as changing the color of the text or making it bold or underlined.
"""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
