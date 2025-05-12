import string

def encrypt(message, shift):
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
    message = message.upper()
    potential_shifts = find_shift(message)
    potential_messages = []
    for shift in potential_shifts:
        potential_messages.append(decrypt_shift(message, shift))
    return potential_messages

def head():
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