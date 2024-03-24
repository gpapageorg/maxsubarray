def maxSubArray(A):
    maxTillNow = 0 
    maxEndingHere = 0
    start, end, s = 0, 0, 0

    n = len(A)
    ri, li = 0, 0
    for i in range(0, n):
        maxEndingHere += A[i]
        if(maxTillNow < maxEndingHere):
            maxTillNow = maxEndingHere
            start = s
            end = i
        
        if maxEndingHere < 0:
            maxEndingHere = 0
            s += 1
    
    print("Max Sum =", maxTillNow)
    print("Start, End =",start, end)

    
    return 
