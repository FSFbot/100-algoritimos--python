def Josephus(n,k):
    if n == 1:
        return 1
    else:
        return (Josephus(n-1,k) + k-1) % n + 1

print(Josephus(41,3))