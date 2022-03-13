from socket import NI_NUMERICSERV
from Core.constants import *


#######################################
# NODES
#######################################

# number node for either int for float
class NumberNode:
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f"{self.tok}>"

# binary node for + - * / operations


class BinaryOperationNode:
    def __init__(self, left_node, operator_token, right_node):
        self.left_node = left_node
        self.operator_token = operator_token
        self.right_node = right_node

    def __repr__(self):
        return f"{self.left_node} {self.operator_token} {self.right_node}"


#######################################
# PARSER
#######################################

# the parser for the language

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens  # the list of tokens
        self.tokenIndex = -1  # the index of the current token
        self.advance()  # advance method for traversing the token list

    def advance(self):
        self.tokenIndex += 1
        if self.tokenIndex < len(self.tokens):
            self.current_token = self.tokens[self.tokenIndex]
        return self.current_token

    # the basic rules method for the parser
    def factor(self):
        tok = self.current_token

        if tok.type in (TT_FLOAT, TT_INT):
            self.advance()
            return NumberNode(tok)

    def term():
        pass

    def expression():
        pass
