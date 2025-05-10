def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = {}
    
    def calculate(index, current_sum):
        if index == n:
            return current_sum == 0 and index > 0
        
        if (index, current_sum) in dp:
            return dp[(index, current_sum)]
        
        include = calculate(index + 1, (current_sum + a[index]) % n)
        exclude = calculate(index + 1, (current_sum - a[index]) % n)
        
        dp[(index, current_sum)] = include or exclude
        return dp[(index, current_sum)]
    
    if calculate(1, a[0] % n) or calculate(1, -a[0] % n):
        print("YES")
    else:
        print("NO")

solve()