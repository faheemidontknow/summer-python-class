# The encrypted message we want to decode
text = 'mrttaqrhknsw ih puggrur'

# The secret key used for the Vigenere cipher
custom_key = 'happycoding'


# Function that does both encryption and decryption
def vigenere(message, key, direction=1):  
    key_index = 0  # Tracks which letter in the key we are on
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # The alphabet we use for shifts
    final_message = ''  # Will store the encrypted or decrypted message

    # Loop through every character in the message
    for char in message.lower():

        # If the character is NOT a letter (like space/punctuation), just add it
        if not char.isalpha():
            final_message += char
        else:        
            # Pick the current letter from the key (it repeats if message is longer than key)
            key_char = key[key_index % len(key)]  
            key_index += 1  # Move to the next key character for next round

            # Get the shift amount based on key character position in the alphabet
            offset = alphabet.index(key_char)  

            # Find the index of the current message character
            index = alphabet.find(char)  

            # Calculate new position:
            #   - For encryption: index + offset
            #   - For decryption: index - offset (because direction = -1)
            new_index = (index + offset * direction) % len(alphabet)  

            # Add the new encrypted/decrypted letter to the final message
            final_message += alphabet[new_index]  
    
    # Return the full result (encrypted or decrypted)
    return final_message  


# Encrypt function (calls vigenere with direction = 1)
def encrypt(message, key):  
    return vigenere(message, key)
    

# Decrypt function (calls vigenere with direction = -1)
def decrypt(message, key):  
    return vigenere(message, key, -1)


# Print out the encrypted text
print(f'\nEncrypted text: {text}')

# Print out the secret key used
print(f'Key: {custom_key}')

# Decrypt the text with the key
decryption = decrypt(text, custom_key)

# Print out the final decrypted message
print(f'\nDecrypted text: {decryption}\n')
