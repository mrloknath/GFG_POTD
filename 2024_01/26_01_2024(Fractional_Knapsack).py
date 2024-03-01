class Solution:    
    def fractionalknapsack(self, W, arr,n):
        curr_weight = 0
        curr_value = 0  
        arr = sorted(arr, key = lambda x: (x.value/x.weight), reverse = True)
        for i in range(n):
            if curr_weight + arr[i].weight <= W: 
                curr_weight += arr[i].weight
                curr_value += arr[i].value
            else:
                accomodate = W - curr_weight 
                value_added = arr[i].value *(accomodate/arr[i].weight)
                curr_value += value_added
                break 
        return curr_value
