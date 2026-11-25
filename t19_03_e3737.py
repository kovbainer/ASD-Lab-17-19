def is_heap(a):
    n = len(a)
    for i in range(1, n + 1):
        if 2 * i <= n and a[i - 1] > a[2 * i - 1]:
            return False
        if 2 * i + 1 <= n and a[i - 1] > a[2 * i]:
            return False
    return True


n = int(input())
a = list(map(int, input().split()))[:n]
print("YES" if is_heap(a) else "NO")
