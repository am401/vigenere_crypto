# Vigenere Crypto
This is a small application that I wrote for a Hacktoberfest 2021 project using a simple [Vigenere Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher), however that script was more of a module as opposed to a standalone script.

I have since turned the script in too a functioning encryption/decryption tool using ArgParse to take command line arguments and text when being used.

# Usage
The usage is rather simple. It uses the `-e` or `--encrypt` flags to encrypt a plain text message. Once set, the script asks for a passphrase. It also utilizes `-d` or `--decrypt` to prompt again for the passphrase when supplying the encrypted message:

```
python3 vigenere_crypto.py -e this is a test
Provide the key to use to encrypt message:
Encrypted message: UHVSVSBTRSG

python3 vigenere_crypto.py -d UHVSVSBTRSG
Provide the key to use to encrypt message:
Encrypted message: THISISATEST
```

As per the above example, when you are prompted for the key, the script does not print to the terminal.

# Caveats
The script removes whitespace, numbers and special characters. I aim to at some point expand to allow for numbers to be incorporated as well, however that is a slightly trickier build. Removing the whitespace has the added benefit that the text merges in to one string and makes it harder to crack as specific words are harder to identify.

The script will strip special characters however it will attempt to use the key provided to encrypt digit. The logic does not exist to then convert the character back to a digit therefore you will get an incorrectly decrypted string.

# Changelog
## [ 0.1 ] - 2021-01-02
### Added
- README.md
