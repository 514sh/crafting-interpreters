from pylox import lox
from pylox.token import Token
from pylox.token_type import (
    Keywords,
    Literals,
    One_or_two_char_tokens,
    Single_char_tokens,
    Special,
)


class Scanner:
    def __init__(
        self,
        source,
    ):
        self._source: str = source
        self._tokens = []
        self._start = 0
        self._current = 0
        self._line = 1

    def scan_tokens(self):
        while not self._is_at_end():
            self._start = self._current
            self._scan_token()

        self._tokens.append(Token(Special.EOF.name, "", None, self._line))
        return self._tokens

    def _scan_token(self):
        char = self._advance()
        for token_type in Single_char_tokens:
            # Comments
            if char == "/" and self._match("/"):
                while self._peek() != "\n" and not self._is_at_end():
                    self._advance()
                return None

            # Single char tokens
            if char == token_type.value:
                self._add_token(token_type.name)
                return None

        # One or Two char tokens
        for token_type in One_or_two_char_tokens:
            if char == token_type.value:
                self._add_token(token_type.name)
                return None

        # Whitespaces
        if char == " ":
            return None
        for c in ["\r", "\t", "\n"]:
            if char == c:
                if char == "\n":
                    self._line += 1
                return None

        # String
        if char == '"':
            self._string()
        elif self._is_digit(char):
            self._number()
        elif self._is_alpha(char):
            self._identifier()
        else:
            lox.error(line=self._line, message="Unexpected character.")
        return None

    def _add_token(self, token_type, literal: str | float | None = None):
        text = self._source[self._start : self._current]
        self._tokens.append(Token(token_type, text, literal, self._line))

    def _advance(self):
        val = self._source[self._current]
        self._current += 1
        return val

    def _is_at_end(self):
        return self._current >= len(self._source)

    def _match(self, expected):
        if self._is_at_end():
            return False
        if self._source[self._current] != expected:
            return False

        self._current += 1
        return True

    def _peek(self):
        if self._is_at_end():
            return "\0"
        return self._source[self._current]

    def _string(self):
        while self._peek() != '"' and not self._is_at_end():
            if self._peek() == "\n":
                self._line += 1
            self._advance()

        if self._is_at_end():
            lox.error(self._line, "Unterminated string.")
            return

        self._advance()

        value = self._source[self._start + 1 : self._current - 1]
        self._add_token(Literals.STRING.name, value)

    def _is_digit(self, char):
        return "0" <= char <= "9"

    def _is_alpha(self, char):
        return ("a" <= char <= "z") or ("A" <= char <= "Z") or char == "_"

    def _is_alphanumeric(self, char):
        return self._is_alpha(char) or self._is_digit(char)

    def _identifier(self):
        while self._is_alphanumeric(self._peek()):
            self._advance()

        text = self._source[self._start : self._current]
        my_token_type = Literals.IDENTIFIER.name
        for token_type in Keywords:
            if text == token_type.value:
                my_token_type = token_type.name
                break
        self._add_token(my_token_type)

    def _number(self):
        while self._is_digit(self._peek()):
            self._advance()

        if self._peek() == "." and self._is_digit(self._peek_next()):
            self._advance()
            while self._is_digit(self._peek()):
                self._advance()

        value = self._source[self._start : self._current]
        self._add_token(Literals.NUMBER.name, float(value))

    def _peek_next(self):
        if self._current + 1 >= len(self._source):
            return "\0"
        return self._source[self._current + 1]
