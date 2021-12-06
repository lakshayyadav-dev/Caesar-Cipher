import string

alphabets = string.ascii_lowercase * 2
encode_inputs = ["encode", "encrypt"]
decode_inputs = ["decode", "decrypt"]
valid_inputs = encode_inputs + decode_inputs


def caesar(cipher_direction, start_text, shift_amount):
    end_text = ""
    if cipher_direction in decode_inputs:
        shift_amount *= -1
    for char in start_text:
        if char in alphabets:
            index = alphabets.index(char)
            new_index = index + shift_amount
            end_text += alphabets[new_index]
        else:
            end_text += char
    print(f"\nText after {cipher_direction}ing is: {end_text}\n")


should_continue = True
while should_continue:
    direction = input("Enter {0} to encrypt or {1} to decrypt: "
                      .format(" or ".join(encode_inputs).casefold(), 
                              " or ".join(decode_inputs))).casefold()
    text = input(f"\nEnter text to {direction}: ").casefold()
    shift = int(input("Enter the shift number: ")) % 26
    caesar(direction, text, shift)

    result = input(
        "Type 'yes' if you want to go again. Type 'no' if you don't: ")
    if result == "no":
        should_continue = False
        print("\nExiting.")
