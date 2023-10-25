def encoder(input1):  # Alex Channing
    output = ""
    for digit in input1:
        x = str((int(digit) + 3) % 10)
        output += x

    return output


def decoder(input1):
    res = ""
    for digit in input1:
        x = str((int(digit) - 3) % 10)
        res += x

    return res
output_1 = ""
output_2 = ""
while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    option = int(input("Please enter an option: "))
    if option == 1:
        encode = str(input("Please enter your password to encode: "))
        output_2 = encode
        output_1 = encoder(encode)
        print("Your password has been encoded and stored!")
    if option == 2:
        decode = decoder(output_1)
        print(f"The encoded password is {output_1}, and the original password is {output_2}.")
    if option == 3:
        break
