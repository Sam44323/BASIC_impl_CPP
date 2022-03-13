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
