from typing import List
from collections import defaultdict

class Solution:
    def kTop(self, arr: List[int], N: int, K: int) -> List[List[int]]:
        ans = []
        mp = defaultdict(int)  # to store frequency
        top = [-1] * (K + 1)

        for i in range(N):
            temp = []

            mp[arr[i]] += 1
            top[K] = arr[i]

            # trying to find the first occurrence of the current element
            ind = -1
            for j in range(K + 1):
                if top[j] == arr[i]:
                    ind = j
                    break

            for j in range(ind - 1, -1, -1):
                if mp[top[j]] < mp[top[j + 1]]:
                    top[j], top[j + 1] = top[j + 1], top[j]
                elif mp[top[j]] == mp[top[j + 1]] and top[j] > top[j + 1]:
                    top[j], top[j + 1] = top[j + 1], top[j]
                else:
                    break

            for j in range(K):
                if top[j] == -1:
                    break
                temp.append(top[j])

            ans.append(temp)

        return ans
