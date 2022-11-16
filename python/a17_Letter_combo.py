def letterCombinations(digits):
    lookup = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz",
    }

    if not digits: return []
    output = [""]

    for d in digits:
        tmp = []
        for v in lookup[d]:
            for o in output:
                tmp.append( o + v )
        output = tmp
    
    return output
 
# Driver code
if __name__ == "__main__" : 

    digits = "23"
    print(letterCombinations(digits))