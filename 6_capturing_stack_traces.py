# we can use the logging module to capture the full stack trace of an application
# by passing exc_info=True as parameter.
# if exc_info is false, the program output will not show the stack trace, just the message.

import logging

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.DEBUG)

is_admin = False

guess_number = input("Enter valid int number:")
try:
    guess_number = int(guess_number)
    # 1-
    logging.info(f"Your number is [{guess_number}]")
    # output#1:
    # root - INFO - Your number is [43] ==> just log record.

    # 2-
    # logging.info(f"Your number is [{guess_number}]", exc_info=True)
    # output#2:
    # root - INFO - Your number is [66]
    # NoneType: None ==> because there is no error found


except ValueError as error:
    # todo: use exc_info=False
    logging.error(f"Invalid number [{guess_number}] [{error}]", exc_info=False)
    # output#3:
    # root - ERROR - Invalid number ds [invalid literal for int() with base 10: 'ds']

    # todo: use exc_info=True
    # logging.error(f"Invalid number {guess_number}", exc_info=True)
    # show full stack trace [traceback] just app in this case works with no crash, it returns code 0. [success]
    # Process finished with exit code 0, but it shows full stack trace like what happens in errors but there is no error
    # app returns code 0 (success)

    # output#4:
    """
    root - ERROR - Invalid number fsd
    Traceback (most recent call last):
      File "E:/containers/learn-projects/python-logging/6_capturing_stack_traces.py", line 13, in <module>
        guess_number = int(guess_number)
    ValueError: invalid literal for int() with base 10: 'fsd'
    """
# ############# ############# ############# ############# ############# ############# ############

x = 10
y = 0

try:
    z = x / y

except ZeroDivisionError:
    logging.exception(f"Can Not Divide '{x}' By '{y}'")  # is equivalent to logging.error(msg, exc_info=True)
    # logging.exception() uses level of ERROR

    # output:

    # logging.exception() uses level of ERROR. [LOOK THIS OUTPUT]
    # logging.exception() is short hand for logging.error() events
    """
    root - ERROR - Can Not Divide '10' By '0'
    Traceback (most recent call last):
        File "E:/containers/learn-projects/python-logging/6_capturing_stack_traces.py", line 52, in <module>
            z = x / y
    ZeroDivisionError: division by zero
    """

# ############# ############# ############# ############# ############# ############# ############

try:
    username = "John"
    age = 25
    info = username + " " + age

except TypeError:
    logging.warning("Invalid contacting. use f-string or format method", exc_info=True)

    # output:
    """
    root - WARNING - Invalid contacting. use f-string or format method
    Traceback (most recent call last):
        File "E:/containers/learn-projects/python-logging/6_capturing_stack_traces.py", line 63, in <module>
            info = username + " " + age
    TypeError: can only concatenate str (not "int") to str
    """
