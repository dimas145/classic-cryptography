class Utils:
    def char_to_idx(self, char):
        return ord(char) - 65 if char.isupper() else ord(char) - 97

    def idx_to_char_upper(self, idx):
        return chr(idx + 65)

    def idx_to_char_lower(self, idx):
        return chr(idx + 97)
