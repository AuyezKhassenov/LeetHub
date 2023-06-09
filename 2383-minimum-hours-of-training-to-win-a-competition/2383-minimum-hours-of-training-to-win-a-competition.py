class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        
        # initialEnergy = 5
        # initialExperience = 3
        # energy = [1,4]
        # experience = [2,5]
        res = 0
        for i in range(len(energy)):
            print('iteration: ',i)
            if initialEnergy <= energy[i]:
                res += energy[i] + 1 - initialEnergy
                initialEnergy = energy[i] + 1
                print('energy: ',energy[i] + 1 - initialEnergy)
            initialEnergy -= energy[i]
            
            if initialExperience <= experience[i]:
                res += experience[i] + 1 - initialExperience
                initialExperience = experience[i] + 1
            initialExperience += experience[i]
            
        return res
                
        