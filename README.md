# Howto
To test and use this code, use a virtualenvironment:

    virtualenv venv
    . venv/bin/activate

Install needed dependencies:

    pip install --editable .

..and you get using

    $ cli --option function

the dialogue ("Something" and "else" is user input):

    Type something: Something
    Something
    Type something else: else
    else
    Option is on
    Functioning

A goal is to get a green test with e.g.

    python -m pytest test_clickprompt.py
