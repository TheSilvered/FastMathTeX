from lexer import Token, TokenKind


class Generator:
    CMD_SUBSTITUTIONS: dict[str, str] = {
        "NN": "mathbb N",
        "ZZ": "mathbb Z",
        "QQ": "mathbb Q",
        "II": "mathbb I",
        "RR": "mathbb R",
        "CC": "mathbb C",
        "ddd": "ldots",  # dot dot dot
        "balign": "begin{align}",
        "ealign": "end{align}",
        "lp": "left(",  # left paren
        "rp": "right)",  # right paren
        "ls": "left[",  # left square bracket
        "rs": "right]",  # right square bracket
        "lc": "left\\{",  # left curly bracket
        "rc": "right\\}",  # right curly bracket
        "ob": "left|",  # open beam
        "cb": "right|",  # close beam
        "al": "alpha",
        "bt": "beta",
        "gm": "gamma",
        "dl": "delta",
        "DL": "Delta"
    }

    def __init__(self, tokens: list[Token]):
        self.tokens = tokens

    def generate(self) -> str:
        s = ""
        for token in self.tokens:
            if token.kind == TokenKind.SPACE:
                s += " "
            elif token.kind == TokenKind.TEXT:
                val = (
                    token.val
                        .replace("\\", "\\\\")
                        .replace("{", "\\{")
                        .replace("}", "\\}")
                )
                s += f"\\text{{{val}}}"
            elif token.kind == TokenKind.ALPHA:
                if len(token.val) == 1:
                    s += token.val
                else:
                    s += "\\" + self.CMD_SUBSTITUTIONS.get(token.val, token.val)
            elif token.kind == TokenKind.OTHER:
                s += token.val
            else:
                raise AssertionError(f"unhandled token kind {token.kind.name}")
        return s.strip()


if __name__ == "__main__":
    from lexer import Lexer
    text = 'forall a_1, a_2, ddd a_n in V "such that" sum_{i=1}^n a_i = 100'
    lex = Lexer(text)
    gen = Generator(lex.tokenize())
    print(gen.generate())
