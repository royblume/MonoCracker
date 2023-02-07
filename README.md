# MonoCracker
Use this python script to crack MonoAlphabetic Substitution Ciphers! 
* python3 MonoCracker.py

For best results, use this python script after completing frequency analysis, in order to identify the remaining words.

Ensure dictionary.txt is present in the folder the script is in.

If you do not have space separated words, remove the commented out print statement in the decode_substitution function to manually check for words.

______________________________________________________________________
## Understanding how to use it
1. If you have fully encrypted or partially encrypted monoalphabetic substitution cipher, you can crack it by entering the cipher into the input with the encrypted characters in upper case (e.g. "hXCp", if "X" and "C" are unknown). 
2. Next, input alphabet characters that have not been assigned to a letter yet (e.g. "e,l,k")
3. The script will then substitute available characters for the encrypted characters and compare it against a dictionary file.

______________________________________________________________________
## Example

EXAMPLE WITH PARTIALLY DECRYPTED CIPHER:
* Partially Decrypted Cipher: teVhnHVal
* Available Substites: c,h,w,q
* --> Decrypted message: technical
* --> Key: [{v:c}, {h:i}]


EXAMPLE WITH FULLY ENCRYPTED CIPHER:
* Fully Encrypted Cipher: ASDF
* Available Substites: p,l,e,h,q,w
* --> Decrypted message: help
* --> Key: [{v:c}, {h:i}]


EXAMPLE WITH PARTIALLY DECRYPTED CIPHER WITH NO SPACES:
* First remove the "#" from the print statement in the decode_substitution function
* Fully Encrypted Cipher: hXDpmX
* Available Substites: e,l
* helpme
* hlepml
