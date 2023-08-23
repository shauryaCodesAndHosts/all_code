from sys import stdin
 
def SmallestSubString (S, n):
    if n <= 1: return n
    freq = dict ()
    distinct_count = len (set (list (S)))
    start_idx = 0; min_len = n + 1
    for j in range (n):
        freq [S [j]] = freq.get (S [j], 0) + 1
        if distinct_count == len (freq): break
    freq [S [j]] -= 1
    for j in range (j, n):
        freq [S [j]] = freq.get (S [j], 0) + 1
        while freq [S [start_idx]] > 1:
            freq [S [start_idx]] -= 1
            start_idx += 1
        new_min = j - start_idx + 1
        if new_min < min_len: min_len = new_min
    return min_len
 
def main ():
    read = stdin.readline
    string = read ().rstrip ()
    n = len (string)
    print (SmallestSubString (string, n))
 
 
if __name__ == "__main__": main ()
