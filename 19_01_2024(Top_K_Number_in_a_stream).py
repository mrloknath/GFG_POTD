class Solution:
    def kTop(self, a, N, K):
        final_ans = []
        top = [0 for i in range(K + 1)]
        freq = {i: 0 for i in range(K + 1)}

        for m in range(N):
            if a[m] in freq.keys():
                freq[a[m]] += 1
            else:
                freq[a[m]] = 1

            top[K] = a[m]
            i = top.index(a[m])
            i -= 1

            while i >= 0:
                if freq[top[i]] < freq[top[i + 1]]:
                    t = top[i]
                    top[i] = top[i + 1]
                    top[i + 1] = t
                elif freq[top[i]] == freq[top[i + 1]] and top[i] > top[i + 1]:
                    t = top[i]
                    top[i] = top[i + 1]
                    top[i + 1] = t
                else:
                    break
                i -= 1

            i = 0
            ans = []
            while i < K and top[i] != 0:
                ans.append(top[i])
                i += 1

            final_ans.append(ans)

        return final_ans
