def max_sum(a,n):
    #code here
    S_0 = sum(i * a[i] for i in range(n))
    sum_a = sum(a)
    max_sum = S_0
    current_sum = S_0
    for k in range(1, n):
        current_sum = current_sum + sum_a - n * a[n - k]
        max_sum = max(max_sum, current_sum)
    return max_sum
