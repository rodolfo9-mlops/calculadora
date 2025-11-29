Calculator
======================

Simple calculator implemented with Python.

---------------------------------------------------------------------

FEATURES
--------
Calculator includes the basic operations:

- Addition
- Subtraction
- Multiplication 
- Division


---------------------------------------------------------------------

PROJECT STRUCTURE
-----------------
```
calculator/
├── src/                     <- code sources
│    ├── __init__.py         <- Configuration file for recognizing the folder as a module
│    ├── test_calculator.py  <- test calculator code
│    ├── calculator/         <- calcualtor code
│    │   ├── __init__.py     <- Configuration file for recognizing the folder as a module
│    │   ├── operations.py   <- python code with basic calculator operations
│    └────── calculadora.py  <- python to use a calculator
├── LICENSE                  <- license example
├── README.md                <- General repository documentation  
├── pyproject.toml           <- setup file
└── requirements.txt                 <- enviroment for testing or packing code
```

---------------------------------------------------------------------

INSTALLATION
------------
    # No specific installation is required.
    
---------------------------------------------------------------------

REQUIREMENTS
------------
- Python 3.10+
- poetry==2.2.1

---------------------------------------------------------------------

SETUP
-----------------

For local development:

    # Create virtual environment
    
    python -m venv venv
    source venv/bin/activate   (On Windows: venv\Scripts\activate)

    # Install dependencies
    
    pip install -r requirements.txt

---------------------------------------------------------------------

RUNNING TESTS
-------------

We can use the python file 'src/test_calculator.py' with the python enviroment created in 'SETUP' section. 

---------------------------------------------------------------------

LICENSE
-------

See the LICENSE file for details.

---------------------------------------------------------------------

AUTHOR
------

Email: example@example.com

GitHub:  https://github.com/rodolfo9-mlops/calculadora