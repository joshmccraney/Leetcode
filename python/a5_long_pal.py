def longestPalSubstr(string):
    maxLength = 1
 
    start   = 0
    length  = len(string)
 
    low     = 0
    high    = 0
 
    # One by one consider every character as center point of
    # even and length palindromes
    for i in range(1, length):
        # Find the longest even length palindrome with center
        # points as i-1 and i.
        low         = i - 1
        high        = i
        while string[low] == string[high] and low >= 0 and high < length:
            low     -= 1
            high    += 1
 
        # Move back to the last possible valid palindrom substring
        # as that will anyway be the longest from above loop
        low         += 1
        high        -= 1
        if high - low + 1 > maxLength:
          start     = low
          maxLength = high - low + 1
 
        # Find the longest odd length palindrome with center
        # point as i
        low         = i - 1
        high        = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            low     -= 1
            high    += 1
 
        # Move back to the last possible valid palindrom substring
        # as that will anyway be the longest from above loop
        low         += 1
        high        -= 1
        if high - low + 1 > maxLength:
            start     = low
            maxLength = high - low + 1
 
    print "Longest palindrome substring is:",
    print string[start:start + maxLength]
 
    return maxLength
 
 
# Driver program to test above functions
string = "racecarijonsd"
print "Length is: " + str(longestPalSubstr(string))


