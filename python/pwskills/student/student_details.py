# why the need of creating different scripts for students and teachers?
# >> To maintain the code, to improve understanding of the code
# best prcatice is to keep different components in different scripts
# example >> model training and EDA should be kept in different scripts
# modules >> A module is a simple file (with .py extention) thatb conatins python code
# inside module functions, class or variable or some python code
# example:> students_details.py and teacher_details.py are modules

# package :: A package is a collection of modules organised in directories
# each directory can have multiple python scripts
# examples >> student and teacher folder is packages
# versions before python 3.3, to make a package it was necessary to include
# __init__.py in package (to initialise package and expose required modules and functions) >> not require any more

# __pycache__ >> also known as pyc file >> These are compiled python files >> source code to byte code >> stored in .pyc file inside __pycache__ directory
# this helps in speedup loading the module next time it is imported
# library >> pre-written code to perform common task>>library is a collection of multiple package and modules
# pandas,numpy

# importing teacher_details module from teacher package
#from teacher import teacher_details # from is used with package, import is used with modules >> generic use from wherever you want to import something from modules/package 
import os, sys # provide functionality to interact with operating system
# sys >> provides access to system specific parameters and function such as python path
from os.path import dirname,join,abspath

# __file__ >> gives path to current script, examples: this script is at d:\Data Science\python\pwskills\student\student_details.py
# dirname >> will give the directory containing the current script
# example: dir(__file__) >> d:\Data Science\python\pwskills\student
# join >> join two or more paths,inserting '/' as needed
#  join(dirname(__file__),"..")) >> move one directory up from the current script directory
# abspath(join(dirname(__file__),".."))) >> abspath converts the relative path to absolute path
parent_dir_path =  abspath(join(dirname(__file__),".."))
sys.path.insert(0,parent_dir_path)
# at index 0, add this directory to the beginning of module search/system path
# it allows to search modules and packages
#from teacher import teacher_details
def student():
    print("This is student details")

#teacher_details.teacher()