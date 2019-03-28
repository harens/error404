# /usr/bin/env python

# This file is part of error404.

# error404 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# error404 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with error404.  If not, see <http://www.gnu.org/licenses/>.

from inspect import stack
from time import time
from os import _exit
import atexit

# Global counter for all tests
number_success = number_failed = total_tests = total_time = 0


def test(function, value):
    """ error404 Default Test Function.

    Concept based on spscah test function
    Note that any data type can be accepted as a value

    Args:
        function: Function to be run
        value: Expected value
    Returns:
        str: Outputs whether test failed/succeeded. If failed, additional information supplied
    """
    start_time = time()  # Time taken
    global total_tests
    total_tests += 1

    # Retrieves info about the caller function from the stack
    line_num = str(stack()[1][2])
    function_name = "".join(stack()[1][4])
    file_name = stack()[1][1]

    # Removes irrelevent info from code_context
    function_name = function_name[
        function_name.index("(") + 1 : function_name.index(",")
    ]

    # If the output was expected
    if function == value:
        print("✅ {0} Succeeded".format(function_name))
        global number_success
        number_success += 1
    else:
        print()
        print(
            "❌ {0} failed at line {1} in {2}".format(function_name, line_num, file_name)
        )
        # Format adds output data types
        print("Program Output:", function, "({0})".format(type(function).__name__))
        print("Expected Output:", value, "({0})".format(type(value).__name__))
        global number_failed
        number_failed += 1
        print()
    global total_time
    # Adds time taken to total time
    total_time += time() - start_time


@atexit.register  # Automatically executed upon normal interpreter termination
def final_output():
    """Overview of test results.

    Provides extended information about how successful the tests were
    Outputted once all tests are complete

    Returns:
        exit(1) if any test fails
    """
    if total_tests != 0:  # Output only if tests were run
        func_time = round(total_time, 4)
        print("\n" * 2)
        if number_failed == 0:
            print(
                "Out of {0} tests, all succeeded in {1} seconds".format(
                    total_tests, func_time
                )
            )
        elif number_success == 0:
            print(
                "Out of {0} tests, all failed in {1} seconds".format(
                    total_tests, func_time
                )
            )
            _exit(1)
        # If some tests failed and others succeeded
        else:
            print(
                "Out of {0} tests, {1} succeeded and {2} failed in {3} seconds".format(
                    total_tests, number_success, number_failed, func_time
                )
            )
            # Success rate rounded to 2 d.p.
            print(
                "This gives a success rate of {0}%".format(
                    round((number_success / total_tests) * 100), 2
                )
            )
            _exit(1)
