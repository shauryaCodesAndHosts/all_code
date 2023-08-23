def bad_character_table(pattern):
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table

def good_suffix_table(pattern):
    table = [0] * (len(pattern) + 1)
    i = len(pattern)
    j = len(pattern) + 1
    
    while i > 0:
        while j <= len(pattern) and pattern[i - 1] != pattern[j - 1]:
            if table[j] == 0:
                table[j] = j - i
            j = table[j]
        i -= 1
        j -= 1
    
    j = table[0]
    for i in range(len(pattern)):
        if table[i] == 0:
            table[i] = j
        if i == j:
            j = table[j]
    
    return table

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    bad_char = bad_character_table(pattern)
    good_suff = good_suffix_table(pattern)
    
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            print("Pattern found at index", i)
            i += good_suff[0]
        else:
            bad_shift = max(1, j - bad_char.get(text[i + j], -1))
            good_shift = good_suff[j + 1]
            i += max(bad_shift, good_shift)

# Example usage
text = "ABAAABCDABAA"
pattern = "ABC"
boyer_moore(text, pattern)
