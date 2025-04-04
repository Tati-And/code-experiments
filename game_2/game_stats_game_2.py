class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, gm_game):
        """Initialize statistics."""
        self.settings = gm_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False
        
        # High score should never be reset.
        self.high_score = 0 
        self.level = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0

        # Start Game_2 in an active state.
        self.game_active = True 