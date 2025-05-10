def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = {}
    
    def calculate(index, current_sum):
        if index == n:
            return current_sum == 0 and index > 0
        
        if (index, current_sum) in dp:
            return dp[(index, current_sum)]
      