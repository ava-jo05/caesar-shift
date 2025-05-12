import string

def encrypt(message, shift):
    """
    Encrypts a message using a Caesar cipher.

    Args:
        message (str): The plaintext message to encrypt.
        shift (int): The number of letters to shift (0-25).

    Returns:
        str: The encrypted message in uppercase.
    """
    message = message.upper()
    shift = shift % 26
    new_message = ""
    for m in message:
        if (not (m in string.ascii_letters)):
            new_message += m
        else:
            new_message += chr((ord(m) - 65 + shift) % 26 + 65)
    return new_message

def decrypt_shift(message, shift):
    """
    Decrypts a message using a Caesar cipher.

    Args:
        message (str): The ciphertext message to decrypt.
        shift (int): The number of letters to shift (0-25).

    Returns:
        str: The decrypted message in uppercase.
    """
    message = message.upper()
    shift = shift % 26
    original_message = ""
    for c in message:
        if (not (c in string.ascii_letters)):
            original_message += c
        else:
            original_message += chr((ord(c) - 65 - shift) % 26 + 65)
    return original_message

def find_shift(text):
    """
    Finds the shift(s) from most common letter in the ciphertext to the most common letters in English text (E, T, A).

    Args:
        text (str): The ciphertext message to find potentials shifts of.

    Returns:
        set: No more than the top three most likely shifts.
    """
    freq = {}
    shift_set = set()
    most_common_letters = ["E", "T", "A"]
    for char in text:
            freq[char] = freq.get(char, 0) + 1
    max_char = max(freq, key=freq.get)
    for i in range(3):
        shift = ord(most_common_letters[i]) - ord(max_char)
        shift_set.add(shift * -1 if shift < 0 else shift)
    return shift_set

def decrypt_unknown_shift(message):
    """
    Generates potential plaintexts of a message using a Caesar cipher when the shift is unknown. 

    Attempts decryption by finding the shift from most common letter in the ciphertext to the most common letters in English text (E, T, A). 

    Args:
        message (str): The ciphertext message to decrypt.

    Returns:
        list: The top three most likely plaintext candidates.
    """
    message = message.upper()
    potential_shifts = find_shift(message)
    potential_messages = []
    for shift in potential_shifts:
        potential_messages.append(decrypt_shift(message, shift))
    return potential_messages

def head():
    """
    A commond-line interface for encrypting and decrypting messages. 

    Features:
        -   Encrypts plaintexts with a known shift. 
        -   Decrypts ciphertexts with a known shift or provides the top three most likely plaintext candidates if the shift is unknown. 
    """
    mode = input("Encrypt or Decrypt? ").strip().lower()
    if (mode == "encrypt"):
        message = input("What would you like to encrypt? ")
        shift = int(input("What is the desired shift? "))
        print("Encrypted: ", encrypt(message, shift))
    elif (mode == "decrypt"):
        message = input("What would you like to decrypt? ")
        know_shift = input("Do you know the key? Type Y/N: ").strip().lower()
        if (know_shift == "y"):
            shift = int(input("What is the key? "))
            print("Decrypted: ", decrypt_shift(message, shift))
        else: 
            decrypted = decrypt_unknown_shift(message)
            print("Here are some potential plaintexts:")
            for d in decrypted:
                print(d)
    return