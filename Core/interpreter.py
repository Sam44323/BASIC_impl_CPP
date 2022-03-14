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
        text = self.text

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

    def token_matcher(self, token_type):
       # compare the current token type with the passed token
       # type and if they match then replace the current token
       # and assign the next token to the self.current_token,
       # otherwise raise an exception

        if self.current_token.type == token_type:
            self.current_token = self.token_advancer()
        else:
            self.error()

    def expression(self):
        """expression -> INTEGER PLUS INTEGER"""
        # setting current token to the first token taken from the input
        (left, right) = (0, 0)
        self.current_token = self.token_advancer()

        while self.current_token.type == INTEGER:
            try:
                left = left * 10 + int(self.current_token.value)
                self.token_matcher(INTEGER)
            except:
                break

        # we expect the current token to be a '+' token

        op = self.current_token
        self.token_matcher(PLUS)

        # we expect the current token to be a single-digit integer

        while self.current_token.type == INTEGER:
            try:
                right = right * 10 + int(self.current_token.value)
                self.token_matcher(INTEGER)
            except:
                break

        # now the self.current_token is set to EOF token
        result = left + right
        return result
