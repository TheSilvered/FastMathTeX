from fastmath import Lexer, Generator
import pyperclip
import readline


if __name__ == "__main__":
    while True:
        line = input('> ')
        if line == "exit":
            break
        lexer = Lexer(line)
        generator = Generator(lexer.tokenize())
        output = generator.generate()
        print(output)
        pyperclip.copy("$" + output + "$")
