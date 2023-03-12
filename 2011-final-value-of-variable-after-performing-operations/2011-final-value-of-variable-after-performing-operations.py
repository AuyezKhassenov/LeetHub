class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        d = {'+': 1, '-' : -1}
        return sum(d[operation[1]] for operation in operations)
        