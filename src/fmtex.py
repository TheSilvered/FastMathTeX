#!/usr/bin/env python3

import pyperclip
import readline
from enum import Enum, auto

from fastmath import fmtex

class FMTeX:
    PROMPT = "> "
    CONTINUATION = "| "
    CMD_START = "'"

    class Mode(Enum):
        INLINE = auto()
        MULTILINE = auto()

    def __init__(self):
        self.mode = self.Mode.INLINE
        self.running = False

    def welcome(self):
        print("Welcome to FastMathTeX!")
        print(f"Type \"{self.CMD_START}exit\" to exit the program.")

    def run(self):
        self.running = True
        self.welcome()

        lines = []
        while self.running:
            prompt = self.PROMPT if not lines else self.CONTINUATION
            line = input(prompt).replace("\r", "").removesuffix("\n")
            if line.startswith(self.CMD_START):
                self.exe_cmd(line)
                continue
            lines.append(line)
            if self.mode == self.Mode.MULTILINE and len(line) != 0:
                continue
            output = fmtex("\n".join(lines))
            print(output)
            self.copy_to_clipboard(output)
            lines = []

    def copy_to_clipboard(self, text: str):
        if self.mode == self.Mode.INLINE:
            pyperclip.copy("$" + text + "$")
        elif self.mode == self.Mode.MULTILINE:
            pyperclip.copy("$$\\begin{align}\n " + text + " \n\\end{align}$$")

    def exe_cmd(self, cmd: str):
        cmd, *args = cmd.strip().removeprefix(self.CMD_START).lower().split()
        if cmd == "exit":
            # Ignore arguments
            self.running = False
        elif cmd == "mode":
            if len(args) == 0:
                print("Current mode:", self.mode.name.lower())
            elif len(args) != 1:
                print("Invalid arguments.")
            else:
                self.change_mode(args[0])
        else:
            print("Unknown command.")

    def change_mode(self, mode: str):
        if "inline".startswith(mode):
            self.mode = self.Mode.INLINE
        elif "multiline".startswith(mode):
            self.mode = self.Mode.MULTILINE
        else:
            print("Unknown mode, valid modes are 'inline' and 'multiline'")


def main():
    prog = FMTeX()
    prog.run()


if __name__ == "__main__":
    main()
