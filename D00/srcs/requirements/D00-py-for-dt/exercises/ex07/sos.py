import sys


# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}


def get_input(morse_code_dict) -> str:
    """
    Retrieves and validates the input from the command line arguments.

    Args:
        morse_code_dict (dict): Dictionary mapping characters to Morse code.

    Returns:
        str: The validated input string in uppercase.

    Raises:
        AssertionError: If the number of arguments is not 2 or if the input
        contains invalid characters.
    """
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    input = sys.argv[1].upper()
    if [c for c in input if morse_code_dict.get(c) is None]:
        raise AssertionError("the arguments are bad")
    else:
        return input


def main(morse_code_dict) -> None:
    """
    Main function to translate input text to Morse code and print the result.

    Args:
        morse_code_dict (dict): Dictionary mapping characters to Morse code.
    """
    try:
        translate = get_input(morse_code_dict)
        encrypted = ' '.join([morse_code_dict[c] for c in translate])
        print(encrypted)
    except AssertionError as e:
        print(f'{AssertionError.__name__}: {e}')
        sys.exit(1)


if __name__ == '__main__':
    main(MORSE_CODE_DICT)
