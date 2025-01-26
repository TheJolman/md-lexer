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

    def _scan_token(self) -> TokenType:
        token = self._advance()
        match token:
            case ".":
                return TokenType.DOT
            case "*":
                match self._match_sequence("*", 3):
                    case 3:
                        self.position += 2
                        return TokenType.STAR_3
                    case 2:
                        self.position += 1
                        return TokenType.STAR_2
                    case _:
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
                match self._match_sequence("#", 4):
                    case 4:
                        self.position += 3
                        return TokenType.HASH_4
                    case 3:
                        self.position += 2
                        return TokenType.HASH_3
                    case 2:
                        self.position += 1
                        return TokenType.HASH_2
                    case _:
                        return TokenType.HASH
            case " " | "\t":
                return TokenType.SPACE
            case "\n":
                return TokenType.NEWLINE
            case _:
                return TokenType.TEXT

    def _advance(self) -> str:
        """Returns current token and advances position by 1"""
        current = self.content[self.position]
        self.position += 1
        return current

    def _peek(self, offset: int = 1) -> str | None:
        """Returns the character at a given offset without advancing the position.
        Args:
            offset: Number of positions ahead to peek. Defaults to 1.
        Returns:
            str: The character at the offset position.
            None: If the offset position is beyond the content length.
        """
        if self._is_at_end(offset):
            return None
        return self.content[self.position + offset]

    def _match_sequence(self, char: str, count: int) -> int:
        """Returns number of consecutive matching characters (up to count)"""
        matches = 1  # current char
        for i in range(1, count):
            if self._peek(i) == char:
                matches += 1
            else:
                break
        return matches

    def _is_at_end(self, offset: int = 0) -> bool:
        """Check if current position is at end of content.
        Args:
            offset: Optional position offset to check. Defaults to 0.
        Returns:
            bool: True if position + offset is at or beyond content length.
        """
        return self.position + offset >= len(self.content)

    def emit_token(self):
        while not self._is_at_end():
            char = self.content[self.position]
            token = self._scan_token()
            print(char, token.name)
