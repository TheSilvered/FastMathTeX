from .lexer import Token, TokenKind


class Generator:
    CMD_SUBSTITUTIONS: dict[str, str] = {
        "NN": "\\mathbb N",
        "ZZ": "\\mathbb Z",
        "QQ": "\\mathbb Q",
        "II": "\\mathbb I",
        "RR": "\\mathbb R",
        "CC": "\\mathbb C",
        "ddd": "\\ldots",  # dot dot dot
        "balign": "\\begin{align}",
        "ealign": "\\end{align}",
        "lp": "\\left(",  # left paren
        "rp": "\\right)",  # right paren
        "ls": "\\left[",  # left square bracket
        "rs": "\\right]",  # right square bracket
        "lc": "\\left\\{",  # left curly bracket
        "rc": "\\right\\}",  # right curly bracket
        "ob": "\\left|",  # open beam
        "cb": "\\right|",  # close beam
        "al": "\\alpha",
        "bt": "\\beta",
        "gm": "\\gamma",
        "dl": "\\delta",
        "DL": "\\Delta",
        "LL": "{",
        "RR": "}"
    }

    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.idx = 0

    def next(self) -> None:
        self.idx += 1

    def prev(self) -> None:
        self.idx -= 1

    @property
    def tok(self) -> Token | None:
        if self.idx < len(self.tokens):
            return self.tokens[self.idx]
        else:
            return None

    def generate(self) -> str:
        s = ""

        while self.tok is not None:
            if self.tok.kind == TokenKind.SPACE:
                s += " "
            elif self.tok.kind == TokenKind.TEXT:
                s += self.generate_text()
            elif self.tok.kind == TokenKind.NUM:
                s += self.tok.val
            elif self.tok.kind == TokenKind.ALPHA:
                s += self.generate_alpha()
            elif self.tok.kind == TokenKind.OTHER:
                s += self.tok.val
            else:
                raise RuntimeError(f"unhandled token kind {self.tok.kind.name}")
            self.next()

        return s.strip()

    def generate_text(self) -> str:
        assert(self.tok is not None and self.tok.kind == TokenKind.TEXT)

        val = (
            self.tok.val
                .replace("\\", "\\\\")
                .replace("{", "\\{")
                .replace("}", "\\}")
        )
        return f"\\text{{{val}}}"

    def generate_alpha(self) -> str:
        assert(self.tok is not None and self.tok.kind == TokenKind.ALPHA)
        assert(len(self.tok.val) > 0)

        if len(self.tok.val) > 1:
            return self.CMD_SUBSTITUTIONS.get(self.tok.val, "\\" + self.tok.val)

        s = self.tok.val
        self.next()
        if self.tok is not None and self.tok.kind == TokenKind.NUM:
            s = "{" + s + "_" + self.tok.val + "}"
        else:
            self.prev()

        return s


if __name__ == "__main__":
    from fastmath.lexer import Lexer
    text = 'forall a1, a2, ddd a_n in V "such that" sum_{i=1}^n a_i = 100'
    lex = Lexer(text)
    gen = Generator(lex.tokenize())
    print(gen.generate())
