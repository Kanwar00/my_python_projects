print("Welcome to Caesar Cypher")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    plain_text = input("Type your message:\n").lower()
    shift_no = int(input("Type the shift number:\n"))



    def encrypt(text, shift):

        encrypted_text = ""
        for letter in text:
            if letter not in alphabet:
                text += letter
            else:
                new_position=alphabet.index(letter) + shift
                encrypted_text += alphabet[new_position%25]
        print(encrypted_text)
    if direction == "encode":
        encrypt(text=plain_text, shift=shift_no)

    def decrypt(text, shift):
        decrypted_text = ""
        for letter in text:
            if letter not in alphabet:
                text += letter
            new_position=alphabet.index(letter) - shift
            decrypted_text += alphabet[new_position%25]
        print(decrypted_text)
    if direction == "decode":
        decrypt(text=plain_text, shift=shift_no)


    go_again = input("Do you want to play again? (y/n)")
    if go_again == "y":
        continue
    elif go_again == "n":
        print("Goodbye")
        break