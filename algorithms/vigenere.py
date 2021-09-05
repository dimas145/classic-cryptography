import re
import random

from .utils import Utils


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


class ExtendedVigenereCipher:
    def __init__(self):
        self.text = ""
        self.key = ""

    def encrypt(self, text, key):
        self.text = text
        self.key = key

        return "".join(
            chr((ord(self.text[i]) + ord(self.key[i % len(self.key)])) % 256)
            for i in range(len(self.text)))

    def decrypt(self, text, key):
        self.text = text
        self.key = key

        return "".join(
            chr((ord(self.text[i]) - ord(self.key[i % len(self.key)])) % 256)
            for i in range(len(self.text)))

    def execute(self, command, text, key):
        if (command == "encrypt"):
            return self.encrypt(text, key)
        else:
            return self.decrypt(text, key)


class FullVigenereCipher:
    def __init__(self):
        self.text = ""
        self.key = ""

    def init_vigenere_square(self):
        self.vigenere_square = [[] for _ in range(26)]

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
                (self.vigenere_square[idx_key][idx_text]))
        return encrypted

    def decrypt(self, text, key):
        self.preprocessing(text, key)

        decrypted = ""
        for i in range(len(self.text)):
            idx_text = Utils.char_to_idx(self.text[i])
            idx_key = Utils.char_to_idx(self.key[i % len(self.key)])

            for j in range(26):
                if self.vigenere_square[idx_key][j] == idx_text:
                    decrypted += Utils.idx_to_char_upper(j)

        return decrypted

    def execute(self, command, text, key):
        if (command == "encrypt"):
            return self.encrypt(text, key)
        else:
            return self.decrypt(text, key)


class AutoKeyVigenereCipher:
    def __init__(self):
        self.text = ""
        self.key = ""

    def preprocessing(self, text, key):
        self.text = re.sub(r'[^a-zA-Z]', '', text).upper()
        self.key = re.sub(r'[^a-zA-Z]', '', key).lower()

    def encrypt(self, text, key):
        self.preprocessing(text, key)

        i = 0
        while len(self.key) < len(self.text):
            self.key += self.text[i]
            i += 1

        encrypted = ""
        for i in range(len(self.text)):
            idx_text = Utils.char_to_idx(self.text[i])
            idx_key = Utils.char_to_idx(self.key[i])
            encrypted += Utils.idx_to_char_upper((idx_text + idx_key) % 26)
        return encrypted

    def decrypt(self, text, key):
        self.preprocessing(text, key)

        decrypted = ""
        j = 0
        for i in range(len(self.text)):
            if i > len(self.key):
                idx_key += decrypted[j]
                j += 1

            idx_text = Utils.char_to_idx(self.text[i])
            idx_key = Utils.char_to_idx(self.key[i])
            decrypted += Utils.idx_to_char_upper((idx_text - idx_key) % 26)
        return decrypted

    def execute(self, command, text, key):
        if (command == "encrypt"):
            return self.encrypt(text, key)
        else:
            return self.decrypt(text, key)
