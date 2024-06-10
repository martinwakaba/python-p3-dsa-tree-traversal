class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        def dfs(node):
            if node is None:
                return None
            if node['id'] == id:
                return node
            for child in node['children']:
                result = dfs(child)
                if result:
                    return result
            return None

  
        return dfs(self.root)

    def get_element_by_id(self, id):
        if self.root is None:
            return None
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            if node['id'] == id:
                return node
            queue.extend(node['children'])

        return None
