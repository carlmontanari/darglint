"""Defines the tokens that result from lexing, as well as their types."""

from enum import Enum


class TokenType(Enum):
    """The possible types of tokens."""

    WORD = 1
    COLON = 2
    DOCTERM = 3  # """
    NEWLINE = 4
    INDENT = 5  # Assumed to always be 4 spaces
    HASH = 6  # A hash mark (for comments/noqa).
    LPAREN = 7  # (
    RPAREN = 8  # )


class Token(object):
    """A token representing anything which can appear in a docstring."""

    def __init__(self,
                 value: str,
                 token_type: TokenType,
                 line_number: int
                 ) -> None:
        """Create a new Token.

        Args:
            value: The value of the token. (The actual string.)
            token_type: The type of token this represents.
            line_number: The line number where this token resides.
                Used when reporting errors.

        """
        self.value = value
        self.token_type = token_type
        self.line_number = line_number

    def __str__(self):
        """Return readable representation for debugging.

        Returns:
            A readable representation for debugging.

        """
        return '<Token {} {}>'.format(self.value, self.token_type)

    def __repr__(self):
        """Return readable representation for debugging.

        Returns:
            A readable representation for debugging.

        """
        return str(self)
