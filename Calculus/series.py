import math

def series(fxn, n, log):
    S = 0
    for i in range(1,n):# starts at n = 1 goes to n
        if log: 
            print(f"at n={i}: {S} (adding f({i}): {fxn(i)})") 
        S += fxn(i)
    print(S)
    return S

S = series(lambda x: pow(x, 1/2), 5, False)