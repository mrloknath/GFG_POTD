class Solution:
    def is_sum_tree(self, node):
        def helper(node):
            if not node:
                return [0,True]
            if not node.left and not node.right:
                return [node.data,True]
            left_val,left_flag =helper(node.left)
            right_val,right_flag=helper(node.right)
            # print(left_val,right_val)
            if node.data!=left_val+right_val or left_flag==False or right_flag==False:
                return [left_val+right_val,False]
            return [node.data,True]
        return helper(node)[1]
