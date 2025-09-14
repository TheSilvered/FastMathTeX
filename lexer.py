from enum import Enum, auto
from typing import Callable

class TokenKind(Enum):
    TEXT = auto()
    SPACE = auto()
    ALPHA = auto()
    OTHER = auto()


class Token:
    def __init__(self, kind: TokenKind, val: str):
        self.kind = kind
        self.val = val

    def __repr__(self):
        return f"{self.__class__.__name__}({self.kind.name}, {self.val!r})"


class Lexer:
    def __init__(self, text: str):
        self.text: str = text
        self.idx = -1

    def next(self) -> str:
        self.idx += 1
        if self.idx < len(self.text):
            ch = self.text[self.idx]
        else:
            ch = ""
        return ch

    def prev(self) -> None:
        if self.idx > 0:
            self.idx -= 1

    @property
    def ch(self) -> str:
        if self.idx < len(self.text):
            return self.text[self.idx]
        else:
            return ""

    def tokenize(self) -> list[Token]:
        tokens: list[Token] = []

        while ch := self.next():
            if ch.isspace():
                tokens.append(self.aggregate(TokenKind.SPACE, str.isspace))
            elif ch.isalpha():
                tokens.append(self.aggregate(TokenKind.ALPHA, str.isalpha))
            elif ch.isdigit():
                tokens.append(self.aggregate(TokenKind.OTHER, str.isdigit))
            elif ch == '"':
                tokens.append(self.raw_text())
            else:
                tokens.append(Token(TokenKind.OTHER, ch))

        return tokens

    def aggregate(self, kind: TokenKind, cond: Callable) -> Token:
        val = self.ch
        while (ch := self.next()) and cond(ch):
            val += ch
        self.prev()

        return Token(kind, val)

    def raw_text(self) -> Token:
        val = ""
        escape = False
        while ch := self.next():
            if ch == '\\':
                escape = True
                continue
            if escape or ch != '"':
                val += ch
            else:
                break
        return Token(TokenKind.TEXT, val)


if __name__ == "__main__":
    tok = Token(TokenKind.OTHER, "test")
    print(tok)
    print([tok, tok])
    text = 'forall a_1, a_2, ddd a_n in V "such that" sum_{i=1}^n a_i = 100'
    lex = Lexer(text)
    print(*lex.tokenize(), sep='\n')
