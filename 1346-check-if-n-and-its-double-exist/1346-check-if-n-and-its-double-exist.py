class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        processed = set()
        for num in arr:
            double = 2*num
            if double in processed:
                return True
            elif not num%2 and num/2 in processed:
                return True
            else:
                processed.add(num)
            
            
        return False
        