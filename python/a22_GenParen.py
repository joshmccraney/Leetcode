def generate(result, s, _open, close, n):
    # Base condition
    if close == n:
        result.append(s)
        return
    # If the number of _open parentheses is less than the given n
    if _open < n:
        generate(result, s + "(", _open + 1, close, n)
    # If we need more close parentheses to balance
    if close < _open:
        generate(result, s + ")", _open, close + 1, n)


def generateParenthesis(n):
    # Resultant list
    result = []
    # Recursively generate parentheses
    generate(result, "", 0, 0, n)
    return result

if __name__ == "__main__":
    n = 4;
    print(generateParenthesis(n))