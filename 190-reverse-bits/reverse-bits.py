class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for _ in range(32):
            # Shift result to left to make space
            result <<= 1
            
            # Add last bit of n to result
            result |= (n & 1)
            
            # Shift n to right
            n >>= 1
        
        return result