# Write your code here
def solve(Arr):
    if 2 * sum(Arr) != N*(N+1):
        return "NO"

    total = 0
    for i in range(len(Arr)):
        a = Arr[i] - i - 1
        total += a

        if total < 0:
            return "NO"
    return "YES"

test_case = int(input())
for case in range(test_case):
    N = int(input())
    Arr = list(map(int, input().split()))

    print(solve(Arr))
