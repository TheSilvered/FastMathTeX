from .lexer import Lexer, Token, TokenKind
from .generator import Generator


def fmtex(text: str):
    lexer = Lexer(text)
    generator = Generator(lexer.tokenize())
    return generator.generate()

