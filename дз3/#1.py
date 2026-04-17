#1
class TreeNode:
    def __init__(self):
        self.count = 0
        self.children = {}
        self.end = False

class Bor:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, s):
        if not s:
            return
        current = self.root
        for i in range(len(s)):
            l = s[i]
            if l not in current.children:
                current.children[l] = TreeNode()
            current = current.children[l]
        current.end = True
        current.count += 1

    def find(self, s):
        current = self.root
        for l in s:
            if l not in current.children:
                return False
            current = current.children[l]
        return current.end

    def delete(self, s):
        if not self.find(s):
            return
        current = self.root
        for l in s:
            current = current.children[l]
        current.count -= 1
        if current.count <= 0:
            current.end = False


