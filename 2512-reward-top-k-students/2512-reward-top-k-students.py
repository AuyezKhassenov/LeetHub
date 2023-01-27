class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        pos, neg = set(positive_feedback), set(negative_feedback) 
        res = []
        
        for rep, sid in zip(report,student_id):
            score = 0
            for word in rep.split(' '):
                if word in pos: score += 3
                if word in neg: score -= 1
            res.append([-score, sid])
        res.sort()
        return [stud for _, stud in res][:k]
        