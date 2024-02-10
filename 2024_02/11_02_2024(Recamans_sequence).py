class Solution:
    def recamanSequence(self, n):
        sequence = [0] * n
        seen = set()
        seen.add(0)
        
        for i in range(1, n):
            if sequence[i - 1] - i > 0 and sequence[i - 1] - i not in seen:
                sequence[i] = sequence[i - 1] - i
                seen.add(sequence[i])
            else:
                sequence[i] = sequence[i - 1] + i
                seen.add(sequence[i])
        
        return sequence
