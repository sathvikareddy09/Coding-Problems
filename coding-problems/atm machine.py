t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    amounts = list(map(int, input().split()))
    result = []
    current_balance = k
    for amount in amounts:
        if current_balance >= amount:
            result.append('1')
            current_balance -= amount
        else:
            result.append('0')
    print("".join(result))
