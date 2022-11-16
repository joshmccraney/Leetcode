def cards(r, b):

    def expVal(r, b):
        if r == 0:
            return 0
        elif b == 0:
            return r
        else:
            return r/(r + b) * (1 + expVal(r-1, b)) + b/(r + b) * (-1 + expVal(r, b-1))

    expVal(r, b)

if __name__ == "__main__":
    r = 26
    b = 26
    cards(r, b)