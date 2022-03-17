from Core.interpreter import Interpreter
# main executor for the program


def main():
    while True:
        try:
            text = input("$pasc> ")
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


main()
