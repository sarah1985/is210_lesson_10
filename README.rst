==========================================
IS 210: Software Application Programming I
==========================================
------------
Homework #08
------------

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Available: 2014-10-27T09:00:00-0400
:Due-Date: 2014-11-03T09:00:00-0400

Overview
========

The following tasks will either have you interacting with existing files in
the starter repo or creating new ones on the fly. Don't forget to add your
interpreter directive, utf-8 encoding, and a short docstring with any new files
that you create!

Task Assignments
================

Tasks 04 - 10
-------------

It is very common in computer programming to create a class to manage the
input and output operation of data stored in a file on the computer's hard
drive. In the following tasks you will create an object that can get,
set and delete other pickled Python objects to and from a file. Make sure to
review Chapter 9 of the text. Lutz covers how to use the native Python pickle
module.


Task 04: Create the PickleCache Class
-------------------------------------

You've already instantiated and used some classes already if you consider
your prior use of such classes like the ``Decimal()`` class. We've also now
covered how to create your own custom classes.

Specifications
^^^^^^^^^^^^^^

#.  Create a file named ``picklecache.py``. In ``picklecache.py``.

#.  Import the ``os`` and ``pickle`` modules.

#.  Initialize the class with a constructor function that accepts a
    ``file_path`` string variable with a default value of ``datastore.pkl``.
    The constructor must also define the following attributes.

    #.  Pseudo-private *class attribute* named ``__file_path``. It must
        assigned the constructor variable ``file_path`` value.
    
    #.  Pseudo-private *class attribute* named ``__file_object`` instantiated
        with ``None``.
    
    #.  Pseudo-private *class attribute* named ``__data`` instantiated as an
        empty dictionary object.

Task 05: Add a Set Method
-------------------------

The ``self.__data`` attribute is pseudo-private and not by convention
accessible to outside objects. Therefore, you will need to create a public
method that allows key value pairs to be stored within the class.

Specifications
^^^^^^^^^^^^^^

#.  Create a bound public function named ``set()`` that accepts two
    arguments: ``key`` and ``value``. It will then save the key pair in the
    ``self.__data`` dictionary.

Task 06: Add a Get Method
-------------------------

You will need a way to retrieve data from the PickleCache object.

Specifications
^^^^^^^^^^^^^^

#.  Create a bound public method named ``get()`` that accepts one argument
    named ``key``. It must use this key to return the requested value from the
    ``self.__data`` dictionary.

#.  Make sure that your use a conditional that check for the existence of
    the key before attempting to return the value.

#.  Print a formatted error statement of ``Error: No value found for key:
    '{}'`` if the key does not exist.

Task 07: Add a Delete Method
----------------------------

There needs to be a way to remove unwanted objects from the ``PickleCache``
object. This method is similar to the previous task but deletes a value instead.

Specifications
^^^^^^^^^^^^^^

#.  Create a bound public method named ``delete()`` that accepts one argument
    named ``key``.

#.  Again you will need to make sure the the provided key exists in the
    ``self.__data`` dictionary object before attempting to delete it. You
    can use the same conditional as you did in *Task 06* or  use *Task 06* as
    part of your conditional check. Either way is fine.

#.  Use the ``del`` statement to remove the key pair from ``self.__data``.

Task 08: Add the Open Method
----------------------------

At this point you have created a standard class that can set,
get and delete objects while the program is running. Now you will make the
data persist by pickling it and saving it to a file. This way the data can be
 accessed the next time the program runs.

You care going to need to use the ``os.path.exists()`` and ``os.path.getsize()``
methods as part of your conditional logic.

Specifications
^^^^^^^^^^^^^^

#.  Create a public bound method named ``open()``. It will not access any
    arguments.

#.  Open the ``self.__file_path`` for reading only if it exists and has a
    file size greater than zero.

    #.  Use conditional flow control to check if the ``self.__file_path``
        exists using ``os.path.exists(self.__file_path)``.

    #.  Check if the file size is greater than zero using ``os.path.getsize
        (self.__file_path)``.

    #.  Use the pickle load function to assign the file contents to the
        ``self.__data`` attribute

    #.  Close the file object.

#.  Re-open the data file in write mode before this function ends.

Task 09: Create a Flush Method
------------------------------

Your class need to be able to save its stored data to file when commanded to
do so. This is especially important if the PickleCache were to be used in a
program running for more than just a few moments. Now you will use the
``pickle.dump()`` method and the file object ``close()`` methods to
accomplish this.

Specifications
^^^^^^^^^^^^^^

#.  Create a bound public function named ``flush`` that has one boolean
    argument named ``reopen`` set to a default of ``True``.

#.  Use the pickle dump methods to save the object's data attribute to the
    object's file object.

#.  Close the file object after the pickle dump.

#.  If the ``reopen`` argument is ``True``, call the ``open()`` method you
    created in the previous task.


Task 09: Create a Flush Method
------------------------------

It is usually a good practice to provide a ``close()`` method for objects
interacting with input and output from files.

Specifications
^^^^^^^^^^^^^^

#.  Create a bound public method named ``close()`` that does not accept any
    arguments.

#.  It should call the ``flush()`` method with ``reopen=False``.



Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Lesson 01.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
.. _Unix Timestamp: https://en.wikipedia.org/wiki/Unix_time
