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


class Token:
    """Represents a single token in the markdown text"""

    def __init__(self, type: TokenType, lexeme: str, line: int, column: int):
        self.type = type
        self.lexeme = lexeme
        self.line = line
        self.column = column

    def __str__(self) -> str:
        return f"Token({self.type.name}, '{self.lexeme}', line={self.line}, col={self.column})"

    def __repr__(self) -> str:
        return self.__str__()


class LexerError(Exception):
    """Custom exception for Lexer errors"""

    pass


class Lexer:
    def __init__(self):
        self.position = 0
        self.line = 1
        self.column = 0
        self.content = ""
        self.token_width = 1

    def read(self, filename: str):
        """Read content from file
        Raises:
            LexerError: If file cannot be read or is empty
        """
        try:
            with open(filename, "r") as file:
                self.content = file.read()
                if not self.content:
                    raise LexerError(f"File '{filename}' is empty")
            self.position = 0
            self.line = 1
            self.column = 0

        except FileNotFoundError:
            raise LexerError(f"File '{filename}' not found")
        except Exception as e:
            raise LexerError(f"Error reading file '{filename}': {str(e)}")

    def _scan_token(self) -> TokenType:
        token = self._advance()
        self.token_width = 1
        match token:
            case ".":
                return TokenType.DOT
            case "*":
                num_stars = self._match_sequence("*", 3)
                self.token_width = num_stars
                match num_stars:
                    case 3:
                        self.position += 2
                        self.token_width = 3
                        return TokenType.STAR_3
                    case 2:
                        self.position += 1
                        self.token_width = 2
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
                num_hashes = self._match_sequence("#", 4)
                self.token_width = num_hashes
                self._advance(num_hashes - 1)
                match num_hashes:
                    case 4:
                        return TokenType.HASH_4
                    case 3:
                        return TokenType.HASH_3
                    case 2:
                        return TokenType.HASH_2
                    case _:
                        return TokenType.HASH
            case " " | "\t":
                return TokenType.SPACE
            case "\n":
                return TokenType.NEWLINE
            case _:
                return TokenType.TEXT

    def _advance(self, offset: int = 1) -> str:
        """Returns current token and advances position by offset (default 1)"""

        if offset < 0:
            raise LexerError("Error: _advance expects an offset >= 0")

        current = self.content[self.position]

        if offset == 0:
            return current

        self.position += 1

        for i in range(offset):
            if current == "\n":
                self.line += 1
                self.column = 0
            else:
                self.column += 1
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
        """Prints tokens with positional information"""
        while not self._is_at_end():
            start_col = self.column

            # First get the token type - this will set token_width
            token_type = self._scan_token()

            # Get the actual lexeme using the determined width
            lexeme = self.content[self.position - self.token_width : self.position]

            token = Token(
                type=token_type, lexeme=lexeme, line=self.line, column=start_col
            )
            print(token)
