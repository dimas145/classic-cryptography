import re

class VigenereCipher:
    
    def __init__(self):
        self.text = ""
        self.key = ""
        
    def char_to_idx(self, char):
        return ord(char)-65 if char.isupper() else ord(char)-97
    
    def idx_to_char_upper(self, idx):
        return chr(idx+65)
    
    def idx_to_char_lower(self, idx):
        return chr(idx+97)
            
    def preprocessing(self, text, key):
        self.text = re.sub(r'[^a-zA-Z]', '', text).upper()
        self.key = re.sub(r'[^a-zA-Z]', '', key).lower()
    
    def encrypt(self, text, key):
        self.preprocessing(text, key)
        
        encrypted = ""
        for i in range(len(self.text)):
            idx_text = self.char_to_idx(self.text[i])
            idx_key = self.char_to_idx(self.key[i % len(self.key)])
            encrypted += self.idx_to_char_upper((idx_text + idx_key) % 26)
        return encrypted
    
    def decrypt(self, text, key):
        self.preprocessing(text, key)
        
        decrypted = ""
        for i in range(len(self.text)):
            idx_text = self.char_to_idx(self.text[i])
            idx_key = self.char_to_idx(self.key[i % len(self.key)])
            decrypted += self.idx_to_char_upper((idx_text - idx_key) % 26)
        return decrypted


