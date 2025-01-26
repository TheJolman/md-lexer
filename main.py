import sys

from lexer import Lexer


def main():
    if len(sys.argv) != 2:
        print("md-lexer version 0.1.0")
        print(f"Usage: python {sys.argv[0]} filename.md")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith(".md") or len(filename) < 4:
        print("Error: Invalid markdown filename")
        sys.exit(1)

    print(f"You entered: {filename}")

    try:
        lexer = Lexer()
        lexer.read(filename)
        lexer.emit_token()
    except Exception as e:
        print(f"Error parsing file: {str(e)}")


if __name__ == "__main__":
    main()
