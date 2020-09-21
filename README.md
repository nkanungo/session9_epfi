Assignment
============
Write separate decorators that:
1. allows a function to run only on odd seconds - 100pts
2. log - 100pts
3. authenticate - 300pts
4. timed (n times) - 100pts
5. Provides privilege access (has 4 parameters, based on privileges (high, mid, low, no), gives access to all 4, 3, 2 or 1 params) - 200pts
Write our htmlize code using inbuild singledispatch - 100pts


These functions has been created to demonstrate the functionality of decorators in python.


def odd_sec_func(sec)
=======================
 

    This function runs only during the odd time 
    Here we are building a small function which only prints and returns the mathematical calculation
    as the output
      
def add(*args)
=================

    implements the decorator

 Question2    
def log_func(fn):
===================
    
    function to demonstrate logging feature
    it logs
    1. The id of the function object called
    2. The doc string of the function
    3. All the local variables used in the function
    
def add_func(*args)
=====================
     returns the sum of the given sequence
    return sum(args)

#Question-3
def authenticate_func():
=========================
  
    This function is created to authenticate the users based on the provided password 
  
    

def auth_factory_func(fn1,user_password)
==========================================
   
    This function takes the password that has been set with the user defined password and 
    checks if the user is authorized to perform the operation
  
#Question-4
def timed_func(reps):
=======================
    This function shows the time elapsed in performing the function
    
#Question-5

def prev_access_func(privilege):
================================
    
    This function Provides privilege access (has 4 parameters, based on privileges 
    (high, medium, low, no), gives access to all 4, 3, 2 or 1 params)
    
    
   
#Question 6
Wrote the htmlize code using inbuild singledispatch
