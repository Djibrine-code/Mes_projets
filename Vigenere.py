```python
def generate_vigenere_table():
    table = []
    for i in range(26):
        row = [(chr((i + j) % 26 + 65)) for j in range(26)]
        table.append(row)
    return table

def encrypt_vigenere(plaintext, key):
    table = generate_vigenere_table()
    key = key.upper()
    plaintext = plaintext.upper()
    ciphertext = ''
    
 key_index = 0
    for char in plaintext:
        if char.isalpha():
            row = ord(key[key_index]) - 65
            col = ord(char) - 65
            ciphertext += table[row][col]
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
            
    return ciphertext
def decrypt_vigenere(ciphertext, key):
    table = generate_vigenere_table()
    key = key.upper()
    ciphertext = ciphertext.upper()
    plaintext = ''
    
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            row = ord(key[key_index]) - 65
            col = table[row].index(char)
            plaintext += chr(col + 65)
            key_index = (key_index + 1) % len(key)
            else:
            plaintext += char
            
    return plaintext
