# error404

[![LGTM Grade](https://img.shields.io/lgtm/grade/python/g/harens/error404.svg?style=for-the-badge)](https://lgtm.com/projects/g/harens/error404/overview/)
[![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/harens/error404.svg?style=for-the-badge)](https://codeclimate.com/github/harens/error404)
[![Codacy grade](https://img.shields.io/codacy/grade/6e4af45add524fbc8b173760e5a72eb0.svg?style=for-the-badge)](https://app.codacy.com/project/harens/error404/dashboard)
[![Latest PyPi release version number](https://img.shields.io/pypi/v/error404.svg?logoColor=violet&style=for-the-badge)](https://pypi.org/project/error404/)
[![PyPi format](https://img.shields.io/pypi/format/error404.svg?style=for-the-badge)](https://pypi.org/project/error404/)
[![Current state (Alpha/Beta/Stable etc.)](https://img.shields.io/pypi/status/error404.svg?style=for-the-badge)](https://pypi.org/project/error404/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/error404.svg?style=for-the-badge)](https://pypi.org/project/error404/)

__*An easy-to-use testing module, that doesn't require the terminal!*__

![Example 1](https://raw.githubusercontent.com/harens/error404/master/art/example1.png)

## Installation
```
pip install error404
```

Or download the project [here](https://github.com/harens/error404/archive/master.zip)

## Usage

For the first parameter of the `test` function, insert the function and its input

Then, add the expected result:
```python
test(some_function(function_input), expected_result)
```

### Locally/In a file
*This example produces the output shown above 👆*

Only the `test` function has to be imported

`test_results` is run at the end to display how many succeeded

```python
from error404 import test

# Example Functions
def add_one(number):
  return number + 1

def reverse_list(user_list):
  return user_list[::-1]
  
# Test Cases
test(add_one(4), 5) # Passes
test(add_one(6), "7") # Fails: Different type
test(add_one(232), 233) # Passes
test(add_one(-2), -1) # Passes

test(reverse_list([1, 2, 3]), [3, 2, 1]) # Passes
test(reverse_list([2, 3]), (3, 2)) # Fails: Different type
```

### Interactive Mode

In interactive mode, you can still use just the `test` function

However, if you want to __restart the counter__, import `clear_results`, which is silent.

If you want to see the __overall results__, import `test_results`. This also runs `clear_results` afterwards.
```python
from error404 import test, test_results
>>> def demo(greeting):
	return greeting

>>> test(demo('hi'), 'hi')
✅ Function (1) Succeeded
>>> test(demo('bye'), 'hello')

❌ Function (2) failed at line 1 in Interactive Mode
Program Output: bye (str)
Expected Output: hello (str)

>>> test_results()

Out of 2 tests, 1 succeeded and 1 failed in 0.4561 seconds
This gives a success rate of 50.0%
```

### Jupyter Notebook/Google Colab

This works similar to a normal file. However, __make sure to run `test_results` or `clear_results` (silent) at the end of the cell__. Otherwise, the counter will continue in the following cells.

## License

This project is licensed under the [GNU General Public License v3.0](https://github.com/harens/error404/blob/master/LICENSE)
