# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, MINUS, MULTI, PLUS, DIV, EOF = 'INTEGER', 'MINUS', 'MULTI', 'PLUS', 'DIV', 'EOF'


class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, MINUS, or EOF
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

##########################################################
# Lexer code                                             #
##########################################################


##########################################################
# Parser / Interpreter code                              #
##########################################################


class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3 + 5", "12 - 5 + 3", etc
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid syntax')

    def token_advancer(self):
        """Advances the `pos` pointer and set the `current_char` variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.token_advancer()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.token_advancer()
        return int(result)

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.token_advancer()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.token_advancer()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.token_advancer()
                return Token(MULTI, '*')

            if self.current_char == '/':
                self.token_advancer()
                return Token(DIV, '/')

            self.error()

        return Token(EOF, None)

    def matcher(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def term(self):
        """Return an INTEGER token value."""
        token = self.current_token
        self.matcher(INTEGER)
        return token.value

    def expression(self):
        """Arithmetic expression parser / interpreter."""
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        result = self.term()  # making sure that the first term/terms are integers
        while self.current_token.type in (PLUS, MINUS, MULTI, DIV):
            operate = self.current_token
            if operate.type == PLUS:
                self.matcher(PLUS)
                result = result + self.term()
            elif operate.type == MINUS:
                self.matcher(MINUS)
                result = result - self.term()
            elif operate.type == MULTI:
                self.matcher(MULTI)
                result = result * self.term()
            elif operate.type == DIV:
                self.matcher(DIV)
                result = result / self.term()

        return result
