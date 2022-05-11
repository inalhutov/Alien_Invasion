class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (33, 40, 77)

        # Настройки корабля
        self.ship_limit = 3
        # Перемещине прешельцев
        self.fleet_drop_speed = 15
        # Настройки пули
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 0, 255, 0
        self.bullets_allowed = 10

        # Темп ускорения игры
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 1.5
        self.fleet_direction = 3
        # Подсчет очко
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
