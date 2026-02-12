import time

class GameState:
    def __init__(self):
        self.total_time = 10 * 60   # 10 minutes
        self.start_time = time.time()   # 🔥 start immediately
        self.current_stage = 2
        self.hints_used = {}        # {stage: count}
        self.max_hints_per_stage = 5

    # ⏳ remaining time
    def time_left(self):
        elapsed = time.time() - self.start_time
        return max(0, int(self.total_time - elapsed))

    # ➖ deduct 10 seconds for hint
    def deduct_time(self, seconds):
        self.total_time = max(0, self.total_time - seconds)

    # 🔁 full reset (auto when time ends)
    def reset(self):
        self.total_time = 10 * 60
        self.start_time = time.time()
        self.current_stage = 2
        self.hints_used = {}

    # ⚠️ reset only when time finishes
    def reset_if_needed(self):
        if self.time_left() <= 0:
            self.reset()


game_state = GameState()
