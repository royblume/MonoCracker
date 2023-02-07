# MonoCracker
Use this python script to crack MonoAlphabetic Substitution Ciphers! 
* python3 MonoCracker.py

For best results, use this python script after completing frequency analysis, in order to identify the remaining words.

Ensure dictionary.txt is present in the folder the script is in.

If you do not have space separated words, remove the commented out print statement in decode_substitution to manually check for words.


______________________________________________________________________
## Example

EXAMPLE WITH PARTIALLY DECRYPTED CIPHER:
* Partially Decrypted Cipher: teVhnHVal
* Available Substites: c,h,w,q
* --> Decrypted message: technical
* --> Key: [{v:c}, {h:i}]


EXAMPLE WITH FULLY ENCRYPTED CIPHER:
* Fully Encrypted Cipher: asdf
* Available Substites: p,l,e,h,q,w
* --> Decrypted message: help
* --> Key: [{v:c}, {h:i}]
