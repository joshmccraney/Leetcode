def value(r):

    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return

def romanToDecimal(str):
    i   = 0;
    res = 0;

    while i < len(str):
        if i + 1 < len(str):
            if value(str[i]) < value(str[i+1]):
                res += value(str[i+1]) - value(str[i])
                i += 2
            else:
                res += value(str[i])
                i += 1
        else:
            res += value(str[i])
            i += 1

    return res

# DRIVER CODE
if __name__ == "__main__":
    str = "MCMIV"
    print(romanToDecimal(str))