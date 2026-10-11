"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""
        
        res = []
        def dfs(node):
            # 记录当前节点值以及它的子节点数量
            res.append(str(node.val))
            res.append(str(len(node.children)))
            for child in node.children:
                dfs(child)
                
        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree."""
        if not data:
            return None
        
        # 将分割后的列表转为迭代器，O(1) 顺序消耗元素
        tokens = iter(data.split(","))
        
        def dfs():
            val = int(next(tokens))
            size = int(next(tokens))
            node = Node(val, [])
            for _ in range(size):
                node.children.append(dfs())
            return node
            
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
