import random

def pi_finder(accu):
    hit = 0.
    for i in range (accu):
        hit = hit + ( (random.random()**2 + random.random()**2) < 1 )
    return (hit/accu) * 4

if __name__ == "__main__":
    for i in range (7):
        print pi_finder (10**i)
