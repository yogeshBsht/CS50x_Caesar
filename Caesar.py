# Caesar

plaintext = input("Enter string to encrypt: ")

# Taking key as input
key = int(input("Enter key: "))
# flag = 1
# while flag:
#     key = input("Enter key: ")
#     if isinstance(key,int):
#         print("Value Error! Key should be an integer.")
#     else: 
#         flag = 0

def encrypt(letter, key):
    if ord(letter)<=90:
        cipher = (ord(letter) + key - ord('A'))%26
        cipher = chr(cipher + ord('A'))
    else:
        cipher = (ord(letter) + key - ord('a'))%26
        cipher = chr(cipher + ord('a'))
    return cipher
    
ciphertext = ''
for letter in plaintext:
    if letter.isalpha():
        cipher = encrypt(letter, key)
    else:
        cipher = letter
    ciphertext += cipher

print(f"plain  text: {plaintext}")    
print(f"cipher text: {ciphertext}")      