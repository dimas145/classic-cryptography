from .utils import Utils

import re


class AffineCipher:
    def __init__(self):
        self.text = ""

    def preprocessing(self, text):
        self.text = re.sub(r'[^a-zA-Z]', '', text).upper()

    def encrypt(self, text, m, b):
        self.preprocessing(text)

        return "".join(
            Utils.idx_to_char_upper((m * Utils.char_to_idx(self.text[i]) + b) %
                                    26) for i in range(len(self.text)))

    def gcd_euclidian(self, a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = self.gcd_euclidian(b % a, a)
        return (g, x - (b // a) * y, y)

    def mod_inv(self, a, m):
        g, x, y = self.gcd_euclidian(a, m)
        return x % m

    def decrypt(self, text, m, b):
        self.preprocessing(text)
        m_inv = self.mod_inv(m, 26)

        return "".join(
            Utils.idx_to_char_upper(m_inv *
                                    (Utils.char_to_idx(self.text[i]) - b) % 26)
            for i in range(len(self.text)))

    def execute(self, command, text, m, b):
        if (command == "encrypt"):
            return self.encrypt(text, m, b)
        else:
            return self.decrypt(text, m, b)
