"""Represents a spongefied string."""
from random import randrange


class SpongeString():
    """Represents a spongefied string.

    A spongefied string is a string where random letters per word
    are capitalized.
    This can be used to mock people online, as the keyboard warrior
    that you are.

    Parameters:
        string(str): The string to spongefy
        spongeness(int): The rate to capitalize letters at per word(1-10)

    Attributes:
        original(str): The original string
        spongeness(int): How much letters to capitalize (1-10)
        sponge_percentage(int): The percentage of a word to spongefy
        text(str): Processed string
    """

    def __init__(self, string, spongeness=6):
        """Construct a spongestring from a string."""
        self.original = string
        self.spongeness = spongeness
        self.sponge_percentage = int(spongeness) * 10
        self.text = self.__spongefy()

    def __spongefy(self):
        """Spongefy ourself.

        Returns:
            str: Spongefied text.
        """
        text = ''

        for word in self.original.split():
            text += self.__process_word(word)
            text += ' '

        return text[:-1]

    def __process_word(self, word):
        """Process a single word in our string.

        Parameters:
            word(String): The word to process

        Returns:
            str: The same word with random capitals
        """
        output = ''
        capitals = self.__capital_positions(word)
        c_index = 0

        for c in word:
            if c_index in capitals:
                output += c.upper()
            else:
                output += c.lower()

            c_index += 1

        return output

    @classmethod
    def __generate_position(cls, word, positions):
        """Find a new random position to capitalize.

        Generates a random position in the word given. If the position is
        already in the list of capitalized positions we recurse into ourself
        to find a new position in the hopes it is not taken.
        If a non-taken position is found return it.

        Parameters:
            word(str): The word we're working on
            positions(list): Current filled positions for this word

        Returns:
            int: New previously-uncapitalized position
        """
        capital_letter_pos = randrange(0, len(word))

        if capital_letter_pos not in positions:
            return capital_letter_pos
        else:
            return cls.__generate_position(word, positions)

    def __capital_positions(self, word):
        """Decide the position of characters to capitalize.

        Decides positions in a word to capitalize randomly.

        Parameters:
            word(str): The word to decide positions for

        Returns:
            list(int): List of integer positions
        """
        capital_amount = int(len(word) * self.sponge_percentage / 100)
        positions = []

        for i in range(0, capital_amount):
            capital_letter = self.__generate_position(word, positions)
            positions.append(capital_letter)

        return positions

    def __repr__(self):
        """Text representation of spongestring."""
        return self.text
