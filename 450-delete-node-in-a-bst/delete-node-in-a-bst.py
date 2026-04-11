class Solution(object):
    def deleteNode(self, root, key):
        
        def findMin(node):
            while node.left is not None:
                node = node.left
            return node
        
        def rdelete(root, key):
            if root is None:
                return None
            
            if key < root.val:
                root.left = rdelete(root.left, key)
            elif key > root.val:
                root.right = rdelete(root.right, key)
            else:
                # Node found
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                
                # ✅ Use MIN from right subtree
                temp = findMin(root.right)
                root.val = temp.val
                root.right = rdelete(root.right, temp.val)
            
            return root
        
        return rdelete(root, key)