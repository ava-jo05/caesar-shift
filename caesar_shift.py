import string

def encrypt():
    message = (input("What's the secret message? ")).upper()
    shift = int(input("What's the desired shift? ")) % 26
    new_message = ""
    for m in message:
        if (m != string.ascii_letters): pass
        new_message += chr((ord(m) - 65 + shift) % 26 + 65)
    return new_message

def find_common_letter(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    max_char = max(freq, key=freq.get)
    shift = ord("E") - ord(max_char) 
    return shift * -1 if shift < 0 else shift

def decrypt():
    cipher = (input("What do you want to decrypt? ")).upper()
    shift = input("Do you know the shift? Type Y/N: ")
    if (shift == "Y"):
        shift = int(input("What's the desired shift? ")) % 26
    else: 
        shift = find_common_letter(cipher)
    original_message = ""
    for c in cipher:
        if (c != string.ascii_letters): pass
        original_message += chr((ord(c) - 65 - shift) % 26 + 65)
    return original_message

def head():
    mode = input("Encrypt or Decrypt? ")
    if (mode == "Encrypt"):
        print("Encrypted: ", encrypt())
    elif (mode == "Decrypt"):
        print("Decrypted: ", decrypt())
    return

head()