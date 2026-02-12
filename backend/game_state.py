import time

class GameState:
    def __init__(self):
        self.total_time = 10 * 60   # 10 minutes
        self.start_time = time.time()
        self.game_active = True

        self.hints_used = {}
        self.max_hints_per_stage = 5

        self.time_up_at = None  # ⏳ When timer hit 0

    # ⏳ remaining time
    def time_left(self):
        if not self.game_active:
            return self.total_time

        elapsed = time.time() - self.start_time
        remaining = max(0, int(self.total_time - elapsed))

        # Detect first time hitting zero
        if remaining == 0 and self.time_up_at is None:
            self.time_up_at = time.time()

        return remaining

    # ➖ deduct time for hints
    def deduct_time(self, seconds):
        self.total_time = max(0, self.total_time - seconds)

    # 🔁 full reset
    def reset(self):
        self.total_time = 10 * 60
        self.start_time = time.time()
        self.game_active = True
        self.hints_used = {}
        self.time_up_at = None

    # ⚠️ auto restart after 2 minutes of TIME UP
    def reset_if_needed(self):
        if self.time_up_at:
            if time.time() - self.time_up_at >= 120:
                self.reset()


game_state = GameState()
