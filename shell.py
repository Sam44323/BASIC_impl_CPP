import Core.Lexer as Lexer

while True:
    text = input('basic > ')
    result, error = Lexer.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)
