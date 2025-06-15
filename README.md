# Time Calculator

This project provides a simple Python utility to calculate the new time after adding a duration to a given start time. It also supports calculating the day of the week after the time addition.

## Overview

The main function `add_time` takes a start time, a duration to add, and optionally the starting day of the week. It returns the new time in 12-hour AM/PM format, including the day of the week if provided, and indicates if the time is on the next day or several days later.

## Usage

```python
from Time Calculator import add_time

# Basic usage without day
new_time = add_time("3:00 PM", "3:10")
print(new_time)  # Output: 6:10 PM

# Usage with day of the week
new_time = add_time("11:30 AM", "2:32", "Monday")
print(new_time)  # Output: 2:02 PM, Monday

# Usage with duration that passes to the next day
new_time = add_time("11:43 AM", "00:20")
print(new_time)  # Output: 12:03 PM

# Usage with duration that passes multiple days
new_time = add_time("10:10 PM", "3:30")
print(new_time)  # Output: 1:40 AM (next day)
```

## Function Signature

```python
def add_time(start, duration, day=''):
    """
    Adds a duration to a start time and returns the new time.

    Parameters:
    - start (str): The start time in "HH:MM AM/PM" format.
    - duration (str): The duration to add in "HH:MM" format.
    - day (str, optional): The starting day of the week (e.g., "Monday").

    Returns:
    - str: The new time in "HH:MM AM/PM" format, optionally with the day of the week and day count.
    """
```

## Additional Information

- The function handles AM/PM time format and converts times accordingly.
- If the day parameter is provided, the function calculates the resulting day of the week.
- The function indicates if the resulting time is on the next day or several days later.

## License

This project is provided as-is without any warranty.
