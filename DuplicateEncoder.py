def duplicate_encode(word):
    #your code here
    res = ''
    arr = [0 for i in range(1000)]
    word = word.lower()
    for w in word:
        arr[ord(w)] += 1
    for w in word:
        if arr[ord(w)] > 1:
            res += ')'
        elif arr[ord(w)] == 1:
            res += '('
    return res