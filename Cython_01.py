import Cython
from Cython.Build import cythonize
from setuptools import setup



def main():
    setup(
        ext_modules = cythonize("hello.pyx")
    )

    print("ok")
    print("nana")
    print("lalal")
    # smth new
    # I want to codding



main()