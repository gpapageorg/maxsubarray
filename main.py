import bruteforce as bf
import lessBruteForce as lbf
import divideAndConquer as dac
import kadanes as kad

import random
import time

def main():
    run()



def run():
    
#####---BRUTEFORMCE---####
    dataFast = genRanList(500)
    dataSlow = genRanList(600)

    print("Now Running BruteForce With Array Length 500")
    start = time.time()
    bf.maxSubArray(dataFast)
    end = time.time()
    print("Time:", round(end - start), "s")
    print()

    print("Now Running BruteForce With Array Length 1000")
    start = time.time()
    bf.maxSubArray(dataSlow)
    end = time.time()
    print("Time:", round(end - start), "s")
    print()

    dataFast = genRanList(3000)
    dataSlow = genRanList(5000)

    print("Now Running LessBruteForce With Array Length 3000")
    start = time.time()
    lbf.maxSubArray(dataFast)
    end = time.time()
    print("Time:", round(end - start), "s")
    print() 

    print("Now Running LessBruteForce With Array Length 5000")
    start = time.time()
    lbf.maxSubArray(dataSlow)
    end = time.time()
    print("Time:", round(end - start), "s")
    print()

    print("Now Running Divide And Conquer With Array Length 700000")
    dataFast = genRanList(700000)
    dataSlow = genRanList(1000000)
    I = [0,0]

    start = time.time()
    meg = dac.maxSubArray(dataFast, 0, len(dataFast) - 1, I)
    end = time.time()
    print("Max Sum:", meg)
    print("Start, End", I[0], I[1])
    print("Time:", round(end - start), "s")
    print()

    print("Now Running Divide And Conquer With Array Length 1000000")

    start = time.time()
    meg = dac.maxSubArray(dataSlow, 0, len(dataSlow) - 1, I)
    end = time.time()
    print("Max Sum:", meg)
    print("Start, End", I[0], I[1])
    print("Time:", round(end - start), "s")

    dataFast = genRanList(7000000)
    dataSlow = genRanList(50000000)

    print("Now Kadane's With Array Length 7000000")
    start = time.time()
    kad.maxSubArray(dataFast)
    end = time.time()
    print("Time:", round(end - start), "s")
    print()

    print("Now Kadane's With Array Length 50000000")

    start = time.time()
    kad.maxSubArray(dataSlow)
    end = time.time()
    print("Time:", round(end - start), "s")
    print()

    

    
def genRanList(length):
    randomlist = []
    for i in range(length):
        n = random.randint(-100,100)
        randomlist.append(n)

    return randomlist

if __name__ == "__main__":
    main()

