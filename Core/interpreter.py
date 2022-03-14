# Token constant definition
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis

PLUS, EOF, INTEGER = 'PLUS', 'EOF', 'INTEGER'


class Token():
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
