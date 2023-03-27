"""
File: install.py
Author: Saúl Sosa Díaz
Date: 23/12/2022
Description: Contains a function named "install" which installs a package using the pip package manager if the user chooses to install it.
"""

import sys
import subprocess

def install(package):
    '''
    If the user wants to install the package, install it. If not, raise an error
    @param package - The name of the package to install.
    '''
    opcion = input("Do you want to install the package: " +
                   package + "? (Y/N): ")
    if opcion.lower() == "y":
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package])
    else:
        raise RuntimeError(package + " has not been installed")
