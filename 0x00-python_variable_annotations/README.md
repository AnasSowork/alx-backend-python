# 0x00. Python - Variable Annotations

This project contains various Python scripts that demonstrate the use of type annotations.

## Files

### 0-add.py
Defines a type-annotated function `add` that takes two floats and returns their sum as a float.

### 1-concat.py
Defines a type-annotated function `concat` that takes two strings and returns their concatenated string.

### 2-floor.py
Defines a type-annotated function `floor` that takes a float and returns the floor of the float as an int.

### 3-to_str.py
Defines a type-annotated function `to_str` that takes a float and returns its string representation.

### 4-define_variables.py
Defines and annotates the following variables:
- `a`: an integer with a value of 1
- `pi`: a float with a value of 3.14
- `i_understand_annotations`: a boolean with a value of True
- `school`: a string with a value of "Holberton"

### 5-sum_list.py
Defines a type-annotated function `sum_list` that takes a list of floats and returns their sum as a float.

### 6-sum_mixed_list.py
Defines a type-annotated function `sum_mixed_list` that takes a list of integers and floats and returns their sum as a float.

### 7-to_kv.py
Defines a type-annotated function `to_kv` that takes a string and an int or float and returns a tuple. The first element is the string, and the second element is the square of the int/float as a float.

### 8-make_multiplier.py
Defines a type-annotated function `make_multiplier` that takes a float multiplier and returns a function that multiplies a float by the multiplier.

### 9-element_length.py
Defines a type-annotated function `element_length` that takes a list and returns a list of tuples, each containing an element and its length.

### 100-safe_first_element.py
Defines a type-annotated function `safe_first_element` that takes a sequence and returns the first element if it exists, otherwise None.

### 101-safely_get_value.py
Defines a type-annotated function `safely_get_value` that takes a dictionary, a key, and a default value. It returns the value associated with the key if it exists, otherwise the default value.

### 102-type_checking.py
Defines a type-annotated function `zoom_array` that takes a tuple and an optional int factor (default is 2), and returns a list where each element of the tuple is repeated `factor` times.

## Main Test Scripts

Each script is accompanied by a main test script to demonstrate its functionality:
- `0-main.py`
- `1-main.py`
- `2-main.py`
- `3-main.py`
- `4-main.py`
- `5-main.py`
- `6-main.py`
- `7-main.py`
- `8-main.py`
- `9-main.py`
- `100-main.py`
- `101-main.py`
- `102-main.py`

## Usage

To run the scripts, ensure you have Python 3.7 or later installed on Ubuntu 18.04 LTS. Each script is executable and can be run directly from the command line.

```sh
$ ./0-main.py
$ ./1-main.py
# And so on for each main script
