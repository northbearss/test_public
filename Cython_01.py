import Cython
from Cython.Build import cythonize
from setuptools import setup



def main():
    setup(
        ext_modules = cythonize("hello.pyx")
    )

    print("ok")



main()