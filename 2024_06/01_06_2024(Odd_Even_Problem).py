class Solution:
    def oddEven(self, s : str) -> str:
        letters_frequency = {}
        for letter in s:
            letters_frequency[letter] = letters_frequency.get(letter, 0) + 1
        
        result = 0
        for key in letters_frequency:
            if ord(key) % 2 == letters_frequency[key] % 2:
                result += 1
        
        if result % 2 == 0:
            return "EVEN"
        return "ODD"
