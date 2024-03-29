# import string
# from this import 
from caesarart import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list


def encrypt(text, shift):
    newtext = ""
    length = len(alphabet)

    for letter in text:
        position = alphabet.index(letter)
        if position + shift <= length - 1:
            position += shift
        else:
            position = position - length + shift 

        newtext += alphabet[position]
    
    print(f"The encoded text is:  {newtext}")
    return newtext

def decrypt(cipher, shift):
    newtext = ""
    length = len(alphabet)

    for letter in cipher:
        position = alphabet.index(letter)
        if position - shift >= 0:
            position -= shift
        else:
            position = position - shift + length 

        newtext += alphabet[position]
    
    print(f"The decrypted text is:  {newtext}")

def caesar(text, shift, direction):
    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)

# if direction == "encode":
#     cipher = encrypt(text, shift)
# else: 
#     decrypt(text, shift)
caesar(text, shift, direction)
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 