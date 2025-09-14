from lexer import Lexer
from generator import Generator
import pyperclip as clip
import readline


if __name__ == "__main__":
    while True:
        line = input('> ')
        if line == "exit":
            break
        lexer = Lexer(line)
        generator = Generator(lexer.tokenize())
        output = generator.generate()
        print(generator.generate())
        clip.copy("$" + output + "$")
