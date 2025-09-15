#!/usr/bin/env python3

from fastmath import Lexer, Generator
import pyperclip
import readline


def main():
    print("Welcome to FastMathTeX!")
    print("Type \"'exit\" to exit the program.")

    while True:
        line = input('> ')
        if line.startswith("'"):
            exe_command(line[1:])
            continue
        lexer = Lexer(line)
        generator = Generator(lexer.tokenize())
        output = generator.generate()
        print(output)
        pyperclip.copy("$" + output + "$")


def exe_command(cmd: str):
    if cmd.strip() == "exit":
        exit()
    else:
        print("Unknown command.")


if __name__ == "__main__":
    main()
