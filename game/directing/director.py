class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def check_for_end_game(self, score, cast):
        """Ends the game based on the score. If the score goes below zero, the 
        player loses. If it gets above 500, the player wins"""

        """Args:
            score (Score): The current score
            cast (Cast): The cast of actors.
            """
        banner = cast.get_first_actor("banners")
        if score <= 0:
            banner.set_text("Sorry, you lost. Maybe you need some more practice...")
        elif score >= 500:
            banner.set_text("You won! How does it feel to be rich??")

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's, gem's, and rock's position and resolves any collisions with objects.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        rocks= cast.get_actors("rocks")
        gems = cast.get_actors("gems")
        
        banner.set_text("Score: ")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for rock in rocks:
            if robot.get_position().equals(rock.get_position()):
                cast.remove_actor("rocks", rock)
            for gem in gems:

                if rock.get_position().equals(gem.get_position()):
                    cast.remove_actor("rocks", rock)

        for gem in gems:
            if robot.get_position().equals(gem.get_position()):
                cast.remove_actor("gems", gem)
                



    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()