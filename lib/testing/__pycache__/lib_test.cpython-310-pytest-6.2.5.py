o
    C^ee  �                   @   s^   d dl Zd dlm  mZ d dlZG dd� d�ZG dd� d�ZG dd� d�Z	G dd	� d	�Z
dS )
�    Nc                   @   �   e Zd ZdZdd� ZdS )�TestNameErrorz
    a_name_error.py
    c                 C   �   t �d� dS )z5
        contains defined name "hello_world"
        zlib/a_name_error.pyN��runpy�run_path��self� r
   �b/home/aloe/Development/Code/Phase3/python-p3-reading-python-error-messages/lib/testing/lib_test.py�test_name_error
   �   zTestNameError.test_name_errorN)�__name__�
__module__�__qualname__�__doc__r   r
   r
   r
   r   r      �    r   c                   @   r   )�TestSyntaxErrorz
    a_syntax_error.py
    c                 C   r   )z(
        multiplies two numbers
        zlib/a_syntax_error.pyNr   r   r
   r
   r   �test_syntax_error   r   z!TestSyntaxError.test_syntax_errorN)r   r   r   r   r   r
   r
   r
   r   r      r   r   c                   @   r   )�TestTypeErrorz
    a_type_error.py
    c                 C   r   )z"
        adds two numbers
        zlib/a_type_error.pyNr   r   r
   r
   r   �test_type_error"   r   zTestTypeError.test_type_errorN)r   r   r   r   r   r
   r
   r
   r   r      r   r   c                   @   r   )�TestAssertionErrorz
    an_assertion_error.py
    c                 C   r   )z,
        evaluates two equal values
        zlib/an_assertion_error.pyNr   r   r
   r
   r   �test_assertion_error.   r   z'TestAssertionError.test_assertion_errorN)r   r   r   r   r   r
   r
   r
   r   r   )   r   r   )�builtins�@py_builtins�_pytest.assertion.rewrite�	assertion�rewrite�
@pytest_arr   r   r   r   r   r
   r
   r
   r   �<module>   s
   "