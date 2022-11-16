def BlackjackHighest(strArr):
    d = {"two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8,
    "nine" : 9, "ten" : 10, "jack" : 10, "queen" : 10, "king" : 10, "ace" : 11}
    value = 0
    lst = [d[card] for card in strArr]
    lst.sort()

    for card in lst:
        value += card
    if value > 21:
        while 11 in lst:
            lst[-1] = 1
            lst.sort()
            value -= 10

    def get_key(val):
        for key, value in d.items():
            if val == value:
                return key

    if value > 21:
        return "above", get_key(lst[-1])
    if value < 21:
        return "below", get_key(lst[-1])
    if value == 21:
        return "blackjack", get_key(lst[-1])

if __name__ == "__main__":
    strArr = ["four","ace","ten"]
    print(BlackjackHighest(strArr))