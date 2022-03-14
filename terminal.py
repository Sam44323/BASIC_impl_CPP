# main executor for the program
def main():
    while True:
        try:
            text = input("$pasc> ")
        except EOFError:
            break
        if not text:
            continue
        print(text)


main()
