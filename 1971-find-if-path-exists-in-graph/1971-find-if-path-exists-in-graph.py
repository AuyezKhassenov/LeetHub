class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        paths = defaultdict(list)
        for edge in edges:
            paths[edge[0]].append(edge[1])
            paths[edge[1]].append(edge[0])
        
        def dfs(node, end, seen):
            if node == end:
                return True
            elif node in seen:
                return False
            
            seen.add(node)
            for n in paths[node]:
                if dfs(n, end, seen):
                    return True
            return False
        seen = set()
        return dfs(source, destination, seen)