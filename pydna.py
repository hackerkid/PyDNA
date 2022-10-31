from collections import Counter

class DNA:
    def __init__(self, string: str):
        self.string = string

    def symbol_count(self):
        return Counter(self.string)
    
    def convert_to_rna(self):
        return self.string.replace("T", "U")
