from Core.interpreter import Interpreter, Lexer
# main executor for the program


def main():
    while True:
        try:
            text = input("$pasc> ")
        except EOFError:
            break
        if not text:
            continue
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expression()
        print(result)


main()
