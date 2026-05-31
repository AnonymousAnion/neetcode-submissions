# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        # Basically, form a string of node values
        # with a separator character and the left
        # child is the current index * 2 + 1 and the
        # right index is the current index * 2 + 2

        serialization = []

        pq = deque()
        pq.append(root)

        while pq:

            current = pq.popleft()
            
            if current:

                serialization.append(str(current.val))
                pq.append(current.left)
                pq.append(current.right)

            else:

                serialization.append("N")

        return ",".join(serialization)
        
    # Decodes your encoded data to a tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        print("Deserializing: ", data)
        data = data.split(",")
        print(data)

        try:
            root_val = int(data[0])
            root = TreeNode(root_val)

        except: 
    
            return None

        pq = deque()
        pq.append(root)
        i = 1

        while pq:

            current = pq.popleft()

            # Left
            try:

                val = int(data[i])
                current.left = TreeNode(val)
                pq.append(current.left)

            except:

                current.left = None

            i += 1

            # Right
            try:

                val = int(data[i])
                current.right = TreeNode(val)
                pq.append(current.right)

            except:

                current.right = None

            i += 1

        return root