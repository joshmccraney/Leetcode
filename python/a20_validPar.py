def isValid(s):
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif stack == [] or dict[char] != stack.pop():
            return False
    return stack == []

if __name__ == "__main__":
    s = "{([[{}]])}"
    print(isValid(s))