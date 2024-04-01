class Solution:
    def merge(self, arr, low, mid, high):
        temp = [0] * (high - low + 1)
        k = 0
        i = low
        j = mid + 1
        inv = 0

        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                k += 1
                i += 1
            else:
                inv += mid - i + 1
                temp[k] = arr[j]
                k += 1
                j += 1

        while i <= mid:
            temp[k] = arr[i]
            k += 1
            i += 1

        while j <= high:
            temp[k] = arr[j]
            k += 1
            j += 1

        for x in range(low, high + 1):
            arr[x] = temp[x - low]

        return inv

    def mergeSort(self, arr, low, high):
        if low >= high:
            return 0

        inv = 0
        mid = (low + high) // 2
        inv += self.mergeSort(arr, low, mid)
        inv += self.mergeSort(arr, mid + 1, high)
        inv += self.merge(arr, low, mid, high)

        return inv

    def inversionCount(self, arr):
        return self.mergeSort(arr, 0, len(arr) - 1)

    def inorder(self, root, arr):
        if root:
            self.inorder(root.left, arr)
            arr.append(root.data)
            self.inorder(root.right, arr)

    def pairsViolatingBST(self, n : int, root : Optional['Node']) -> int:
        # code here
        arr = []
        self.inorder(root, arr)
        return self.inversionCount(arr)
        
