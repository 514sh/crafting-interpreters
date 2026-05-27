from enum import Enum


class TokenType(Enum):
    pass


class Single_char_tokens(TokenType):
    # Single char tokens
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"
    COMMA = ","
    DOT = "."
    MINUS = "-"
    PLUS = "+"
    SEMICOLON = ";"
    SLASH = "/"
    STAR = "*"


class One_or_two_char_tokens(TokenType):
    BANG_EQUAL = "!="
    EQUAL_EQUAL = "=="
    GREATER_EQUAL = ">="
    LESS_EQUAL = "<="
    BANG = "!"
    EQUAL = "="
    GREATER = ">"
    LESS = "<"


class Keywords(TokenType):
    AND = "and"
    CLASS = "class"
    ELSE = "else"
    FALSE = "false"
    FUN = "fun"
    FOR = "for"
    IF = "if"
    NIL = "nil"
    OR = "or"
    PRINT = "print"
    RETURN = "return"
    SUPER = "super"
    THIS = "this"
    TRUE = "true"
    VAR = "var"
    WHILE = "while"


class Literals(TokenType):
    IDENTIFIER = ""
    STRING = '"'
    NUMBER = ""


class Special(TokenType):
    EOF = ""
