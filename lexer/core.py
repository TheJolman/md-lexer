from enum import Enum, auto
import pdb

class TokenType(Enum):
    DOT = auto()
    STAR = auto()
    UNDERSCORE = auto()
    DASH = auto()
    GREATER = auto()
    PIPE = auto()
    BACKSLASH = auto()
    HASH = auto()
    TEXT = auto()
    SPACE = auto()
    NEWLINE = auto()

class Lexer:
    def __init__(self):
        pass

    def read(self, filename: str):
        self.content: str
        with open(filename, 'r') as file:
            self.content = file.read()

    def _lex(self, token: str):
        match token:
            case '.':
                return TokenType.DOT
            case '*':
                return TokenType.STAR
            case '_':
                return TokenType.UNDERSCORE
            case '-':
                return TokenType.DASH
            case '>':
                return TokenType.GREATER
            case '|':
                return TokenType.PIPE
            case '\\':
                return TokenType.BACKSLASH
            case '#':
                return TokenType.HASH
            case ' ' | '\t':
                return TokenType.SPACE
            case '\n':
                return TokenType.NEWLINE
            case _:
                return TokenType.TEXT

    def emit_token(self):
        for char in self.content:
            token = self._lex(char)
            print(char, token.name)

