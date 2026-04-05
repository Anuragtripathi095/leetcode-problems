class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Edge case
        if numerator == 0:
            return "0"
        
        result = []
        
        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')
        
        # Work with positive values
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Integer part
        result.append(str(numerator // denominator))
        remainder = numerator % denominator
        
        # If no remainder → no decimal part
        if remainder == 0:
            return ''.join(result)
        
        result.append('.')
        
        # Map to store remainder → index
        remainder_map = {}
        
        while remainder != 0:
            # If remainder repeats → cycle detected
            if remainder in remainder_map:
                index = remainder_map[remainder]
                result.insert(index, '(')
                result.append(')')
                break
            
            # Store remainder position
            remainder_map[remainder] = len(result)
            
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        
        return ''.join(result)