# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com


class ROT13Coder:
    letters = "abcdefghijklmnopqrstuvwxyz"
    number_of_letters = len(letters)
    letters_map = dict(zip(list(letters), range(number_of_letters)))
    shift = 13

    def encode_symbol(self, original_symbol):
        if not original_symbol.isalpha():
            return original_symbol

        encoded_symbol = None
        letter_position = ROT13Coder.letters_map[original_symbol.lower()]

        if letter_position + ROT13Coder.shift > ROT13Coder.number_of_letters - 1:
            encoded_symbol = ROT13Coder.letters[ROT13Coder.shift - (ROT13Coder.number_of_letters - letter_position)]
        else:
            encoded_symbol = ROT13Coder.letters[letter_position + ROT13Coder.shift]

        return encoded_symbol if original_symbol.islower() else encoded_symbol.upper()

    def encode(self, original_text):
        encoded_text = str()
        for symbol in original_text:
            encoded_text += self.encode_symbol(symbol)

        return encoded_text
