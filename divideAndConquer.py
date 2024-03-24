def maxSumCrossingMiddle(A, l, m, h, I):
    currSum = 0
    leftSum = float('-inf')
    
    for i in range (m, l - 1, -1):
        currSum += A[i]

        if (currSum > leftSum):
            leftSum = currSum
            lm = i


    currSum = 0
    rightSum = float('-inf')

    for i in range (m + 1, h + 1):
        currSum += A[i]

        if (currSum > rightSum):
            rightSum = currSum
            rm = i

    meg = float('-inf')

    if ( rightSum + leftSum > meg ):
        meg = rightSum + leftSum
        I[0] = lm
        I[1] = rm
    if ( leftSum > meg):
        I[0] = lm
        I[1] = m
    if ( rightSum > meg):
        I[0] = m
        I[1] = rm

            
    return max(rightSum + leftSum, leftSum, rightSum)

def maxSubArray(A, l, h, I):
    
    if (l == h):
        return A[l]

    m = (l + h) // 2

    meg = float("-inf")

    Il, Ih, Ic = [0,0], [0,0], [0,0]


    a = maxSubArray(A, l, m,Il)   
    b = maxSubArray(A, m + 1, h,Ih)
    c = maxSumCrossingMiddle(A, l, m, h, Ic)
    
    if (a > meg):
        meg = a
        I[0] = Il[0]
        I[1] = Il[1]

    if (b > meg):
        meg = b
        I[0] = Ih[0]
        I[1] = Ih[1]

    if (c > meg):
        meg = c
        I[0] = Ic[0]
        I[1] = Ic[1]

    return meg 
