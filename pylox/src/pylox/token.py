class Token:
    def __init__(self, token_type, lexeme, literal, line):
        self._token_type = token_type
        self._lexeme = lexeme
        self._literal = literal
        self._line = line

    def __str__(self):
        return f"line {self._line}: type - {self._token_type} | lexeme - {self._lexeme} | literal - {self._literal}"
