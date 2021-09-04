from .utils import Utils

import re


class AffineCipher:
    def __init__(self):
        self.text = ""
        self.valid_m = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

    def preprocessing(self, text):
        self.text = re.sub(r'[^a-zA-Z]', '', text).upper()

    def encrypt(self, text, m, b):
        self.preprocessing(text)
        if (m not in self.valid_m):
            return

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
