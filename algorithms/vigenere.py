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
