import argparse
import getpass
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='Vigenere Cipher encryption and decryption tool.')
    parser.add_argument('-e', '--encrypt', dest='encrypt', nargs='*', help='Enter text to encrypt.')
    parser.add_argument('-d', '--decrypt', dest='decrypt', nargs='*', help='Enter text to decrypt.')
    args = parser.parse_args()

    # Check and exit if no arguments have been passed to the tool.
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    else:
        return args


def create_key(msg, key):
    """Create teh key that will be used to encrypt the message.
    The first check ensures that if the message and key length
    are the same, return the key value. Otherwise ensure that
    a long enough key is generated via the for loop."""
    key = list(key)
    if len(msg) == len(key):
        return key
    elif len(key) < len(msg):
        n = (len(msg) // len(key)) + 1
        key = key * n
        return ''.join(key[:len(msg)])


def encrypt(msg, key):
    """Function to encrypt the provided message using the
    defined key. The msg is looped through one character
    at a time and using the key the encrypted text is
    generated."""
    cipher_text = []
    x = 0
    key = create_key(msg, key)
    for i in range(0, len(msg)):
        x = (ord(msg[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return cipher_text


def decrypt(msg, key):
    """Much like the above encrypti function, this
    function uses the existing encrypted text to loop
    through and subtract the key value to get the original
    plain text character."""
    key = create_key(msg, key)
    plain_text = []
    for i in range(0, len(msg)):
        x = (ord(msg[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        plain_text.append(chr(x))
    return plain_text


def check_key_length(msg, key):
    """If the key is longer than the message, terminuate
    the script from running and provide an error message
    to the user."""
    key_length = len(key)
    msg_length = len(msg)
    if msg_length < key_length:
        print("Error: the key cannot be longer than the message.")
        sys.exit()
    
if __name__ == '__main__':
    args = parse_args()
    if args.encrypt:
        msg = "".join(args.encrypt).upper().replace(" ", "")
        key = getpass.getpass(prompt='Provide the key to use to encrypt message: ')
        key = key.upper().replace(" ", "")
        check_key_length(msg, key)
        cipher_text = encrypt(msg, key)
        print("Encrypted message:", "".join(cipher_text))
    elif args.decrypt:
        msg = "".join(args.decrypt).upper().replace(" ", "")
        key = getpass.getpass(prompt='Provide the key to use to encrypt message: ')
        key = key.upper().replace(" ", "")
        check_key_length(msg, key)
        plain_text = decrypt(msg, key)
        print("Encrypted message:", "".join(plain_text))
