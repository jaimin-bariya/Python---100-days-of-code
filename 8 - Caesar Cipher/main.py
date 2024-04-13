from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, text, shift):

    shift = shift % 26


    result = ""


    if direction == "decode":
        shift *= -1

    for letter in text:
        if letter == " ":
            result += " "
        else:
            position = alphabet.index(letter)
            new_position = position + shift
            result += alphabet[new_position]
            
    
    print(f"your {direction}d text is : {result} ")



isGameOn = True

print(logo)

while(isGameOn):
    user_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    user_text = input("Type your message:\n").lower()
    user_shift = int(input("Type the shift number:\n"))


    caesar(direction=user_direction, text=user_text, shift=user_shift)

    gameContinue = input("Type yes to start again, No to quit : \n").lower()

    if gameContinue == "no":
        print("Good Bye")
        isGameOn = False

