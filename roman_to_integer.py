class Solution(object):
        
    @staticmethod
    def roman_to_integer(s: str) -> int:
        rules = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        total = rules[s[n-1]]
        
        for i in range(n-1, 0, -1):
            current = rules[s[i]]
            prev = rules[s[i-1]]
            total += prev if prev >= current else - prev
            
        return total


solution = Solution()

print(solution.roman_to_integer("III"))
print(solution.roman_to_integer("IV"))
print(solution.roman_to_integer("IX"))
print(solution.roman_to_integer("LVIII"))
print(solution.roman_to_integer('MCMXCIV'))
