class Solution:
    def sumBitDifferences(self, arr, n):
        # Initialize the result
        result = 0

        # Traverse over all bits
        for i in range(32):
            # Count the number of elements with i'th bit set
            count_set_bit = 0
            for j in range(n):
                if (arr[j] & (1 << i)):
                    count_set_bit += 1

            # Count the number of elements with i'th bit unset
            count_unset_bit = n - count_set_bit

            # Add the bit differences for this position to the result
            result += count_set_bit * count_unset_bit * 2

        return result
