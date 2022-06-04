from winreg import REG_OPTION_BACKUP_RESTORE


class Score(): 

    def __init__(self):
        """Intitialies the score as well as changes the font to normal"""
        self._score1 = 1 
        self.score_font = pygame.font.SysFont(None,100)
        

    def get_score(self):
        """gets score"""
        return self._score1
    
    def update_score(self):

        robot = cast.get_first_actor("robots")
        rocks= cast.get_actors("rocks")
        gems = cast.get_actors("gems")

        self._totalscore = Score().get_score()
        if robot.get_position().equals(rock.get_position()):
            self._totalscore -= 30
        elif rock.get_position().equals(gem.get_position()):
            self._totalscore +=20 
        
        return self._totalscore
    
    
        

        

                
                
        

