--- TOOL DESCRIPTION --- 

This is my implementation of a Caesar shift cipher. 

Overall, this projects allows users to encrypt and decrypt messages by shifting the letters according to a specified shift or key. 
However, users can still attempt to decrypt a ciphertext when the shift is unknown. By nature, shift ciphers are easy to break because there are only 26 possible keys. 
Decryption can be efficiently attempted by finding the shift from most common letter in the ciphertext to the most common letters in English text (E, T, A). 

This tool also offers a command-line interface for encrypting messages.

--- HOW TO USE TOOL ---

To run a specific function, run:
python -c "import caesar_shift; caesar_shift.<function>"

For example:
>>> python -c "import caesar_shift; caesar_shift.encrypt('Top Secret!', 8)" 

To run a specific function and print the outut, run:
python -c "import caesar_shift; print(caesar_shift.<function>)"

For example:
>>> python -c "import caesar_shift; print(caesar_shift.encrypt('Top Secret!', 8))"
BWX AMKZMB!

To use the command-line interace, run:
python -c "import caesar_shift; caesar_shift.head()"

--- HOW TO RUN TESTS ---

To checkout my test cases, run:
python -m unittest test_caesar_shift.py

To checkout a specific test case, run:
python -m unittest test_caesar_shift.TestCaesarShift.<test_method>

For example:
python -m unittest test_caesar_shift.TestCaesarShift.test_encrypt_1

The above line runs the first encryption test case where the message is "ABC" and the shift is 3. 

--- FUTURE IMPROVEMENTS ---

If I had more time, I would like to support lowercase and case-sensitive messages. 
This would increase the amount of ciphertexts and plaintexts users are able to generate and decode. 