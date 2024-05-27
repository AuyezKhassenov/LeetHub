class Solution:
    def simplifyPath(self, path: str) -> str:
        elements = []
        path = path.split('/')
        for p in path:
            if p == '..':
                if not elements:
                    continue
                else:
                    elements.pop()
            elif p == '.' or p == '':
                continue
            else:
                elements.append(p)
        return '/' + '/'.join(elements)