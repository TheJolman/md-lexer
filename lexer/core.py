from enum import Enum

class TokenType(Enum):
    DOT = '.'
    STAR = '*'
    UNDERSCORE = '_'
    DASH = '-'
    GREATER = '>'


def lexer(filename: str):
    """Open a markdown file for reading and print all tokens."""

    with open(filename, 'r') as file:
        content = file.read()

    print(content)


