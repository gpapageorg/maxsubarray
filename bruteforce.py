def maxSubArray(A):
    s = 0
    f = 0
    maxSum = float("-inf")
    n = len(A)

    for i in range(0, n):
        for j in range(i, n):
            currSum = 0
            for k in range(i, j + 1):
                currSum += A[k]
            a = maxSum 
            maxSum = max(maxSum, currSum)
            if (maxSum != a):
                s = i
                f = j

    print("Max Sum =", maxSum)
    print("Start, End =", s, f)
