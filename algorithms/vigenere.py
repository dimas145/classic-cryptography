import re
import random

from utils import Utils


class VigenereCipher:
    def __init__(self):
        self.text = ""
        self.key = ""

    def preprocessing(self, text, key):
        self.text = re.sub(r'[^a-zA-Z]', '', text).upper()
        self.key = re.sub(r'[^a-zA-Z]', '', key).lower()

    def encrypt(self, text, key):
        self.preprocessing(text, key)

        encrypted = ""
        for i in range(len(self.text)):
            idx_text = Utils.char_to_idx(self.text[i])
            idx_key = Utils.char_to_idx(self.key[i % len(self.key)])
            encrypted += Utils.idx_to_char_upper((idx_text + idx_key) % 26)
        return encrypted

    def decrypt(self, text, key):
        self.preprocessing(text, key)

        decrypted = ""
        for i in range(len(self.text)):
            idx_text = Utils.char_to_idx(self.text[i])
            idx_key = Utils.char_to_idx(self.key[i % len(self.key)])
            decrypted += Utils.idx_to_char_upper((idx_text - idx_key) % 26)
        return decrypted

    def execute(self, command, text, key):
        if (command == "encrypt"):
            return self.encrypt(text, key)
        else:
            return self.decrypt(text, key)


class FullVigenereCipher:
    def __init__(self):
        self.text = ""
        self.key = ""
        self.init_vigenere_square()

    def init_vigenere_square(self):
        self.vigenere_square = [[] for i in range(26)]

        for i in range(26):
            self.vigenere_square[i] = random.sample(
                "abcdefghijklmnopqrstuvwxyz", 26)

            for j in range(26):
                self.vigenere_square[i][j] = Utils.char_to_idx(
                    self.vigenere_square[i][j])

    def preprocessing(self, text, key):
        self.text = re.sub(r'[^a-zA-Z]', '', text).upper()
        self.key = re.sub(r'[^a-zA-Z]', '', key).lower()

    def encrypt(self, text, key):
        self.preprocessing(text, key)

        encrypted = ""
        for i in range(len(self.text)):
            idx_text = Utils.char_to_idx(self.text[i])
            idx_key = Utils.char_to_idx(self.key[i % len(self.key)])
            encrypted += Utils.idx_to_char_upper(
                (self.vigenere_square[idx_text][idx_key]) % 26)
        return encrypted

    def decrypt(self, text, key):
        self.preprocessing(text, key)

        decrypted = ""
        for i in range(len(self.text)):
            idx_text = Utils.char_to_idx(self.text[i])
            idx_key = Utils.char_to_idx(self.key[i % len(self.key)])
            decrypted += Utils.idx_to_char_upper(
                (self.vigenere_square[idx_key][idx_text]) % 26)
        return decrypted

    def execute(self, command, text, key):
        if (command == "encrypt"):
            return self.encrypt(text, key)
        else:
            return self.decrypt(text, key)
