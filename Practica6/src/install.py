import sys
import subprocess

def install(package):
    '''
    Make sure that the package is installed regardless of the machine running the program.
    Parameters:
    package (string): Name of the package to install.
    '''
    opcion = input("Do you want to install the package: " +
                   package + "? (Y/N): ")
    if opcion.lower() == "y":
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package])
    else:
        raise RuntimeError(package + " has not been installed")
