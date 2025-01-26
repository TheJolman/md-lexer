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
