def maxSubArray(A):
    maxSum = float('-inf')
    n = len(A)
    s = 0
    f = 0

    for i in range(0, n):
        currSum = 0
        for j in range(i, n):
            currSum += A[j]
            a = maxSum
            maxSum = max(maxSum, currSum) 
            if (maxSum != a):
                s = i
                f = j


    print("Max Sum =", maxSum)
    print("Start, End =",s, f)
