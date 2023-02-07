from itertools import permutations, product

def decode_substitution(ciphertext, key):
    original = ""
    for char in ciphertext:
        if char in key:
            if char.isupper():
                original += key[char]
            else:
                original += char
        else:
            original += char
    #print(original.lower())
    """
    Remove the comment from the print statement if you do not have space separated words to manually check for real words
    """
    return original.lower()

def generate_keys(chars, subs):
    keys = []
    
    
    for permutation in permutations(subs):
        key = {char: permutation[i] for i, char in enumerate(chars)}
        keys.append(key)
    return keys

def extract_encrypted(encrypted_text):
    partial = list(encrypted_text)
    encrypted_values = []
    for char in partial:
        if char.isupper():
            if char not in encrypted_values:
                encrypted_values.append(char)
    return encrypted_values

def key_generator(encrypted_word, decoded_word):
    keys = []
    for i in range(len(encrypted_word)):
        if encrypted_word[i] != decoded_word[i]:
            key = {encrypted_word[i]:decoded_word[i]}
            keys.append(key)
    return keys
def main():
    print("""
        

        ___  ___                  _____                _             
        |  \/  |                 /  __ \              | |            
        | .  . | ___  _ __   ___ | /  \/_ __ __ _  ___| | _____ _ __ 
        | |\/| |/ _ \| '_ \ / _ \| |   | '__/ _` |/ __| |/ / _ \ '__|
        | |  | | (_) | | | | (_) | \__/\ | | (_| | (__|   <  __/ |   
        \_|  |_/\___/|_| |_|\___/ \____/_|  \__,_|\___|_|\_\___|_|   
                                                                     
                                                                     


        Example input:
        Partially Encrypted message: enXrIpted
        Available substitution characters: c,y
        Decrypted message: encrypted
        Key: [{x:c}, {i:y}]



        """)
    ciphertext = input("Enter the partially encrypted message, with the encrypted characters in CAPS: ")
    encrypted_chars = extract_encrypted(ciphertext)
    available_subs = input("Enter available substitution characters, separated by a comma: ")
    available_subs = available_subs.split(",")
    keys = generate_keys(encrypted_chars, available_subs)
    with open("dictionary.txt", "r") as f:
        words = set(line.strip() for line in f)
    for key in keys:
        decoded = decode_substitution(ciphertext, key)
        decoded_words = decoded.split()
        if all(word in words for word in decoded_words):
            print("Decrypted message: ", decoded)
            print("Key: ", key_generator(ciphertext.lower(),decoded))
            break

if __name__ == "__main__":
    main()