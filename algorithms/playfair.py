from collections import OrderedDict
from .utils import Utils

import re


class PlayFairCipher:
    def __init__(self) -> None:
        self.text = ""
        self.key = ""
        self.bigram = []
        self.key_matrix = [-1 for _ in range(25)]

    def init_key_matrix(self, key):
        key = re.sub(r'[^a-zA-Z]', '', key).upper()

        key = "".join(OrderedDict.fromkeys(key))

        cnt = 0
        for i in range(len(key)):
            if key[i] != "J":
                self.key_matrix[cnt] = Utils.char_to_idx(key[i])
                cnt += 1

        for i in range(26):
            if i != 9 and Utils.idx_to_char_upper(i) not in key:
                self.key_matrix[cnt] = i
                cnt += 1

    def create_bigram_list(self, text):
        self.bigram = []
        i = 0
        while i < len(text):
            if i == len(text) - 1:
                self.bigram.append([
                    Utils.char_to_idx(text[i]),
                    Utils.char_to_idx("X"),
                ])
                i += 1
            elif text[i] == text[i + 1]:
                self.bigram.append([
                    Utils.char_to_idx(text[i]),
                    Utils.char_to_idx("X"),
                ])
                i += 1
            else:
                self.bigram.append([
                    Utils.char_to_idx(text[i]),
                    Utils.char_to_idx(text[i + 1]),
                ])
                i += 2

    def preprocessing(self, text, key):
        self.text = re.sub(r'[^a-zA-Z]', '', text).upper()
        self.key = re.sub(r'[^a-zA-Z]', '', key).lower()

    def encrypt(self, text, key):
        self.preprocessing(text, key)
        self.init_key_matrix(self.key)

        # replace j with i
        self.text.replace("J", "I")

        # create bigram list
        self.create_bigram_list(self.text)

        encrypted = ""
        for i in range(len(self.bigram)):
            first = self.key_matrix.index(self.bigram[i][0])
            second = self.key_matrix.index(self.bigram[i][1])

            if first // 5 == second // 5:
                # same row
                first = first - 4 if first % 5 == 4 else first + 1
                second = second - 4 if second % 5 == 4 else second + 1
            elif first % 5 == second % 5:
                # same column
                first = first - 20 if first // 5 == 4 else first + 5
                second = second - 20 if second // 5 == 4 else second + 5
            else:
                # rectangular pattern
                new_first = first // 5 * 5 + second % 5
                second = second // 5 * 5 + first % 5

                first = new_first

            encrypted += Utils.idx_to_char_upper(self.key_matrix[first])
            encrypted += Utils.idx_to_char_upper(self.key_matrix[second])

        return encrypted

    def decrypt(self, text, key):
        self.preprocessing(text, key)
        self.init_key_matrix(self.key)

        decrypted = ""
        for i in range(0, len(self.text), 2):
            first = self.key_matrix.index(Utils.char_to_idx(self.text[i]))
            second = self.key_matrix.index(Utils.char_to_idx(self.text[i + 1]))

            if first // 5 == second // 5:
                # same row
                first = first + 4 if first % 5 == 0 else first - 1
                second = second + 4 if second % 5 == 0 else second - 1
            elif first % 5 == second % 5:
                # same column
                first = first + 20 if first // 5 == 0 else first - 5
                second = second + 20 if second // 5 == 0 else second - 5
            else:
                # rectangular pattern
                new_first = first // 5 * 5 + second % 5
                second = second // 5 * 5 + first % 5

                first = new_first

            decrypted += Utils.idx_to_char_upper(self.key_matrix[first])
            decrypted += Utils.idx_to_char_upper(self.key_matrix[second])

        # remove meaningless X?

        return decrypted

    def execute(self, command, text, key):
        if (command == "encrypt"):
            return self.encrypt(text, key)
        else:
            return self.decrypt(text, key)
