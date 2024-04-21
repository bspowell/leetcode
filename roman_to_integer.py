# place all symbols and their values within a hash
# include special cases:
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# iterate over the string
# if I
#   check if next letter is V - return 4
#   check if next letter is X - return 9
# if X 
#   check if next letter is L - return 40
#   check if next letter is C - return 90
# if C
#   check if next letter is D - return 400
#   check if next letter is M - return 900


# Time complexity: O(N)
# Space complexity: O(N)


def romanToInt(s):
    roman_hash = { 
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    }
    total = 0
    i = 0
  
    while i < len(s):
        total += roman_hash[s[i]] 

        if i + 1 < len(s) and s[i:i+2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
            if s[i:i+2] == 'IV':
                total += 3
            elif s[i:i+2] == 'IX':
                total += 8
            elif s[i:i+2] == 'XL':
                total += 30
            elif s[i:i+2] == 'XC':
                total += 80
            elif s[i:i+2] == 'CD':
                total += 300
            elif s[i:i+2] == 'CM':
                total += 800
              
            i += 2
        else:
            i += 1
    return total



print(romanToInt('III')) # 3
print(romanToInt('LVIII')) # 58
print(romanToInt('MCMXCIV')) # 1991


