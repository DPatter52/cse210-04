from winreg import REG_OPTION_BACKUP_RESTORE
from game.casting.cast import Cast
from tkinter import messagebox



class Score(): 

    def __init__(self):
        """Intitialies the score as well as changes the font to normal"""
        self._score1 = 500 
        

    def get_score(self):
        """gets score"""
        return self._score1
    
    def update_score(self, collision):
        self._totalscore = self.get_score() 

        if collision == "inRocks":
            self._totalscore -= 30
        elif collision == "inGems":
            self._totalscore += 20
        else: 
            self._totalscore = self._totalscore


        #for rock in rocks:
            #if robot.get_position().equals(rock.get_position()):
                #self._totalscore -= 30
                

        #for gem in gems:
            #if robot.get_position().equals(gem.get_position()):
                #self._totalscore += 20
                
                

        self._score1 = self._totalscore
        return self._score1
        
    
        

        

                
                
        

