# Happy Pi Day Nerds!

Pi day is 3/14 (March 14). So here's a python script to generate digits of pi.
It uses the [Chudnovski algorithm](https://en.wikipedia.org/wiki/Chudnovsky_algorithm).

## Running the Script

### Prerequisites:

- Make sure you have Python version 3 installed. You can download it from [python.org](https://www.python.org/downloads/)

- Also, make sure the `pi_day.py` file has execute permission. If not, change the file permissions by running the following command (in a unix/mac environment):

   ```bash
   chmod +x pi_day.py
   ```

### Run the script

The script can be run from any command line.

1. Navigate to the directory where the script is located.

2. Execute the script as:

   ```bash
   python3 pi_day.py
   ```

3. Alternatively, you can execute the script as:

   ```bash
   ./pi_day
   ```

## Changing the Number of Digits

Currently, the script is set to display the first 15000 digits of pi. You can change the number of digits by changing the `disp` parameter
in the PI function (line 6 in the script).
