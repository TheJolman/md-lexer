from token_type import TokenType

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
