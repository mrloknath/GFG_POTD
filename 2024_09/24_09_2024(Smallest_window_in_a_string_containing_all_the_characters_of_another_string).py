class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        from collections import Counter
        p_count = Counter(p)
        required = len(p_count)
        left, right = 0, 0
        formed = 0
        window_counts = {}
        
        min_length = float('inf')
        min_left = 0
        
        while right < len(s):
            character = s[right]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            if character in p_count and window_counts[character] == p_count[character]:
                formed += 1
            while left <= right and formed == required:
                character = s[left]
                
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left
                
                window_counts[character] -= 1
                if character in p_count and window_counts[character] < p_count[character]:
                    formed -= 1
                
                left += 1
            
            right += 1

        return s[min_left:min_left + min_length] if min_length != float('inf') else "-1"

