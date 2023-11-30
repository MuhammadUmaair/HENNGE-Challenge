# HENNGE Challenge Solutions

This repository contains my solutions to the HENNGE Challenge, a programming challenge hosted by HENNGE. The challenge involves various coding problems that assess skills in algorithms, data structures, and problem-solving.

## Table of Contents

- [Introduction](#introduction)
- [Solutions](#solutions)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository includes solutions to challenges posed by HENNGE, demonstrating my programming skills and problem-solving abilities.

## Solutions

1. [**Mission 1.py**](https://github.com/MuhammadUmaair/HENNGE-Challenge/blob/main/Mission1.py): Python script for computing the sum of squares of non-negative integers for multiple test cases.

## sum_of_squares_non_negative(nums) Function:

This function takes a list of integers (nums) as input.
Initializes a variable total to store the sum of squares of non-negative integers.
Iterates through each number in the input list:
If the number is non-negative (greater than or equal to zero), it squares the number and adds it to the total.
Returns the final total sum.

## main() Function:

Takes the number of test cases as input (num_test_cases).
Processes each test case:
Reads the number of integers in the test case (num_integers).
Reads a line of integers, splits it, and converts the input into a list of integers (integers).
Calls the sum_of_squares_non_negative() function with the list of integers obtained for the current test case.
Prints the result obtained from the sum_of_squares_non_negative() function for each test case.

## if __name__ == "__main__": block:

This block ensures that the main() function is executed when the script is run directly (not when it's imported as a module).
Overall, this script reads input data containing test cases, each consisting of a list of integers, computes the sum of squares of non-negative integers for each test case, and prints the result for each case.

![image](https://github.com/MuhammadUmaair/HENNGE-Challenge/assets/104490047/e5229b27-54d3-4376-9689-a32f55e5b382)



2. [**Mission 3.py**](https://github.com/MuhammadUmaair/HENNGE-Challenge/blob/main/Mission3.py): 

## Imports:

import hashlib: Library for cryptographic hashing functions.
import time: Provides various time-related functions.
import base64: Deals with Base64 encoding and decoding.
import pyotp: Library for generating one-time passwords (OTP).
from pyotp.utils import build_uri: Importing a specific function build_uri from pyotp.utils.

## Variables Initialization:

secret_key = 'HENNGECHALLENGE003': A secret key used for generating the OTP.
msg = 'codetest57@gmail.com': An email address string, likely used as part of the data for OTP generation.
key = msg + secret_key: Concatenating the email address and the secret key.

## Encoding:

bytearray(key, 'ascii'): Converts the concatenated string key into a byte array using ASCII encoding.
base64.b32encode(...): Encodes the byte array into Base32 encoding.

## OTP Generation:

pyotp.TOTP(...): Creates a Time-based One-Time Password (TOTP) instance.
Parameters:
base64.b32encode(...): The encoded key from the previous step.
digits=10: Specifies the number of digits in the generated OTP (10 in this case).
digest=hashlib.sha512: Specifies the hash function to use (SHA512 in this case).
passw = pyotp.TOTP(...) creates an OTP object based on the provided parameters.

## Generating OTP:

passwz = passw.now(): Generates the current one-time password using the TOTP object created earlier.
Output:

print(passwz): Prints the generated one-time password to the console.
time.sleep(5): Pauses the program for 5 seconds.
print(passw.verify(passwz)): Verifies if the generated OTP (passwz) is valid at the current time using the passw.verify(...) function. This line prints either True or False based on the OTP's validity.
```
This code essentially generates a one-time password (OTP) using TOTP based on a secret key and an email address. It then prints the generated OTP and checks its validity after a 5-second delay. The OTP is generated using a combination of the secret key and the email address, and it's validated against the current time.
```

![image](https://github.com/MuhammadUmaair/HENNGE-Challenge/assets/104490047/e74f275d-f8f3-4070-a60f-9d4f452de742)




## Getting Started

Include instructions on how to get a copy of the project up and running on a local machine.

```

git clone https://github.com/MuhammadUmaair/HENNGE-Challenge.git
cd hennge-challenge

```

## Contributing

If you'd like to contribute, fork the repository and create a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
