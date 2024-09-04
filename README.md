# Time Calculator

Welcome to the **Time Calculator**! This Python-based terminal application allows users to manipulate time by adding or subtracting hours, minutes, and seconds.

## Features

- Add UI

## How to Use

### 1. Set the Start Time

After launching the program, you will be prompted to enter the start time. You'll input hours, minutes, seconds, and whether it's AM or PM.

- If you press `Enter` without entering anything, the default value `00` is set for hours, minutes, and seconds, and `AM` is set for the time period.

### 2. Modify Time

After setting the start time, you can:
- Add or subtract time.
- Input time to add or subtract in hours (`h`), minutes (`m`), or seconds (`s`). 
  - For example: `1.5h` for 1.5 hours, `90m` for 90 minutes, `45s` for 45 seconds.

### 3. Exit

You can exit the program at any time by selecting the exit option from the menu.

## Example

```bash
$ python3 time_calculator.py
========================================
   Welcome to the Time Calculator App!   
========================================
You can add or subtract time easily.
Let's get started!

Enter hours (0-12) [default 00]: 2
Enter minutes (0-59) [default 00]: 30
Enter seconds (0-59) [default 00]: 
Enter AM or PM [default AM]: PM

Current time: 02:30:00 PM

Choose an action:
1. Add time
2. Subtract time
3. Exit
Enter your choice (1, 2, 3): 1
Enter time to add (e.g., '1.5h', '90m', '45s'): 2h

Current time: 04:30:00 PM

Choose an action:
1. Add time
2. Subtract time
3. Exit
Enter your choice (1, 2, 3): 3

Exiting...

```



## Requirements

Python 3.x

## Installation

Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/time_calculator.git
```

Navigate to the project directory:
```bash
cd time_calculator
```

Run the code
```bash
python3 time_calculator.py
```

## Contributing
If you'd like to contribute to the project, feel free to fork the repository and submit a pull request. Issues and suggestions are also welcome!

