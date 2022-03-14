# Token constant definition
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis

import string
from tokenize import String


PLUS, EOF, INTEGER = 'PLUS', 'EOF', 'INTEGER'


class Token:
    def __init__(self, type, value) -> None:
        self.type = type  # INTEGER, PLUS, or EOF
        self.value = value  # value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None

    def __repr__(self) -> str:
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )


class Interpreter:
    def __init__(self, text) -> None:
        self.text = text  # example: 10 + 5
        self.pos = 0  # the current position in the text
        self.current_token = None  # the current token

    def error(self):
        raise Exception('Error parsing input')

    def token_advancer(self):
        """Lexical analyzer

          This method is responsible for breaking a sentence
          apart into tokens. One token at a time.
        """
        text = self.current_token

        if self.pos > len(text) - 1:
            return Token(EOF, None)

        curr_char = text[self.pos]

        if curr_char.isdigit():
            token = Token(INTEGER, int(curr_char))
            self.pos += 1
            return token

        elif curr_char == '+':
            token = Token(PLUS, curr_char)
            self.pos += 1
            return token

        self.error()  # throw error if none of the condition matches
