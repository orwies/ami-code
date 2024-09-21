from consts import CODE_DICTIONARY


def get_decoded(char):
    if char in CODE_DICTIONARY:
        return CODE_DICTIONARY[char]

    if char.isdigit():
        return " "

    return char


def decode_and_reverse_words(encoded_content):
    decoded_chars = [get_decoded(char) for char in encoded_content]
    joined_string = "".join(decoded_chars)
    reversed_words = joined_string.split(" ")
    decoded_content = " ".join(word[::-1] for word in reversed_words)

    return decoded_content


def main():
    with open("code.text") as ami_code:
        encoded_content = ami_code.read()
        decoded_content = decode_and_reverse_words(encoded_content)
        print(decoded_content)


if __name__ == "__main__":
    main()
