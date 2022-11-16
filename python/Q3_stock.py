def MinWindowSubstring(strArr):
    s = strArr[0]
    t = strArr[1]

    counter_t = {}
    counter_s = {}
            
    for c in t:
        counter_t[c] = counter_t.get(c, 0) + 1

    i = 0
    j = 0
    
    left = -1
    right = -1
    
    valid = 0
    
    for i in range(len(s)):
        
        while j < len(s) and valid < len(counter_t):
            counter_s[s[j]] = counter_s.get(s[j], 0) + 1
            
            if s[j] in counter_t and counter_s[s[j]] == counter_t[s[j]]:                    
                valid += 1  
            j += 1 
        
        if valid == len(counter_t):
            if left == -1 or j - i < right - left:
                left = i
                right = j   
        
        counter_s[s[i]] -= 1
        if s[i] in counter_t and counter_s[s[i]] == counter_t[s[i]] - 1:
            valid -= 1
            
    if left == -1:
        return ""   
           
    return s[left : right]

if __name__ == "__main__":
    strArr = ["ahffaksfajeeubsne", "jefaa"]
    print(MinWindowSubstring(strArr))