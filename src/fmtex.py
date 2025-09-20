#!/usr/bin/env python3

import pyperclip
try:
    import gnureadline as readline
except ImportError:
    import readline
import re
from enum import Enum, auto

from fastmath import fmtex

class FMTeX:
    class Mode(Enum):
        INLINE = auto()
        MULTILINE = auto()

    def __init__(self):
        self.mode = self.Mode.INLINE
        self.running = False
        self.lines: dict[int, str] = {}

    def welcome(self):
        print("Welcome to FastMathTeX!")
        print(f"Type \"'exit\" to exit the program and \"'help\" for more commands.")

    def input_hook(self):
        def hook():
            if self.mode == self.Mode.MULTILINE:
                readline.insert_text(f"{self.next_line_idx()}> ")
                readline.redisplay()
        return hook

    def run(self):
        self.running = True
        self.welcome()

        readline.set_pre_input_hook(self.input_hook())

        while self.running:
            line = self.get_input_line()
            if line[1].startswith("'"):
                self.exe_cmd(line[1])
                readline.remove_history_item(readline.get_current_history_length() - 1)
                continue
            self.lines[line[0]] = line[1]
            if self.mode == self.Mode.MULTILINE and len(line[1]) != 0:
                continue
            output = fmtex("\n".join(ln[1] for ln in self.line_list()))
            print(output)
            self.copy_to_clipboard(output)
            self.lines = {}

    def next_line_idx(self):
        return (len(self.lines) + 1) * 10

    def get_input_line(self) -> tuple[int, str]:
        prompt = "> " if self.mode == self.Mode.INLINE else "| "
        line = input(prompt).replace("\r", "").removesuffix("\n")
        if self.mode == self.Mode.INLINE:
            return (self.next_line_idx(), line)

        line_match = re.match(r"^\s*(\d+)\s*>.*", line)
        if line_match is None:
            return (self.next_line_idx(), line)
        return (int(line_match.group(1)), line.split(">", 1)[1].removeprefix(" "))

    def line_list(self) -> list[tuple[int, str]]:
        return list(sorted(self.lines.items(), key=lambda x: x[0]))

    def copy_to_clipboard(self, text: str):
        if self.mode == self.Mode.INLINE:
            pyperclip.copy("$" + text + "$")
        elif self.mode == self.Mode.MULTILINE:
            pyperclip.copy("$$\\begin{align}\n " + text + " \n\\end{align}$$")

    def exe_cmd(self, cmd: str):
        cmd, *args = cmd.strip().removeprefix("'").lower().split()
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
        elif cmd == "list":
            if len(args) == 0:
                for ln in self.line_list():
                    print(f"  {ln[0]}  {ln[1]}")
            else:
                print("Invalid arguments.")
        elif cmd == "clear":
            print("\x1b[2J\x1b[3J\x1b[H")
        elif cmd == "help":
            print("Commands:")
            print("'help          display this message")
            print("'exit          exit the program")
            print("'mode <mode>   change the mode (inline or multiline)")
            print("'list          list the current lines")
            print("'clear         clear the screen")
            print()
            print("To change a previous line in multiline mode, delete the line number")
            print("and replace it with the desired one.")
            print("To add a line in between ad a number between the two lines.")
        else:
            print("Unknown command.")

    def change_mode(self, mode: str):
        self.lines = {}
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
