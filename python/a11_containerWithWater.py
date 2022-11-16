def waterHeight(H):
    ans, i, j = 0, 0, len(H)-1
    while (i < j):
        if H[i] <= H[j]:
            area = H[i] * (j - i)
            i += 1
        else:
            area = H[j] * (j - i)
            j -= 1
        if area > ans:
            ans = area
    return ans

# DRIVER CODE
H = [1,8,6,2,5,4,8,3,7]
print(waterHeight(H))