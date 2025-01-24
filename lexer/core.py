import pdb
from enum import Enum, auto


class TokenType(Enum):
    """Tokens belonging to the markdown markup language"""

    DOT = auto()
    STAR = auto()
    STAR_2 = auto()
    STAR_3 = auto()
    UNDERSCORE = auto()
    DASH = auto()
    GREATER = auto()
    PIPE = auto()
    BACKSLASH = auto()
    HASH = auto()
    HASH_2 = auto()
    HASH_3 = auto()
    HASH_4 = auto()
    TEXT = auto()
    SPACE = auto()
    SPACE_SPACE = auto()
    NEWLINE = auto()


class Lexer:
    def __init__(self):
        pass

    def read(self, filename: str):
        self.position = 0
        self.content: str
        with open(filename, "r") as file:
            self.content = file.read()

    def _scan_token(self):
        token = self._advance()
        match token:
            case ".":
                return TokenType.DOT
            case "*":
                return TokenType.STAR
            case "_":
                return TokenType.UNDERSCORE
            case "-":
                return TokenType.DASH
            case ">":
                return TokenType.GREATER
            case "|":
                return TokenType.PIPE
            case "\\":
                return TokenType.BACKSLASH
            case "#":
                num_hashes = self._match_sequence("#", 4)
                match num_hashes:
                    case 4:
                        return TokenType.HASH_4
                        self.position += 3
                    case 3:
                        return TokenType.HASH_3
                        self.position += 2
                    case 2:
                        return TokenType.HASH_2
                        self.position += 1
                    case _:
                        return TokenType.HASH
            case " " | "\t":
                return TokenType.SPACE
            case "\n":
                return TokenType.NEWLINE
            case _:
                return TokenType.TEXT

    def _advance(self) -> str:
        """Returns next token"""
        self.position += 1
        return self.content[self.position]

    def _peek(self, offset: int = 1) -> str | None:
        """Returns next token without advancing, with optional offset (default 1)"""
        if self._is_at_end(offset):
            return None
        return self.content[self.position + offset]

    def _match_sequence(self, char: str, count: int) -> int:
        """Returns number of consecutive matching characters (up to count)"""
        matches = 1  # current char
        for i in range(1, count):
            if self._peek(count) == char:
                matches += 1
            else:
                break
        return matches

    def _is_at_end(self, offset: int = 0) -> bool:
        """Checks if the current position at the end of content or out of bounds with
        Optional offset
        """
        return self.position + offset >= len(self.content)

    def emit_token(self):
        for char in self.content:
            token = self._scan_token(char)
            print(char, token.name)
