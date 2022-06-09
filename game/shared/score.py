
class Score(): 

    def __init__(self):
        """Intitialies and updates the score"""
        self._score1 = 500 
        

    def get_score(self):
        """gets score"""
        return self._score1
    
    def update_score(self, collision):
        self._totalscore = self.get_score() 

        if collision == "inRocks":
            self._totalscore -= 100
        elif collision == "inGems":
            self._totalscore += 100
        else: 
            self._totalscore = self._totalscore         

        self._score1 = self._totalscore
        return self._score1
        
    
        

        

                
                
        

