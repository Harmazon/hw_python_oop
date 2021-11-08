class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def show_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * Training.LEN_STEP / Training.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.get_distance / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        info = InfoMessage(self.duration(), self.get_distance(),
                           self.get_mean_speed(), self.get_spent_calories())
        return info


class Running(Training):
    """Тренировка: бег."""
    def get_spent_calories(self) -> float:
        cf_cal1 = 18
        cf_cal2 = 20
        cal_run = (cf_cal1 * self.get_mean_speed()
                   - cf_cal2) * self.weight / Training.M_IN_KM * self.duration
        return cal_run


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self, action: int, duration: float,
                 weight: float, height: float) -> float:
        super().__init__(action, duration, weight)
        self.height = height
        cf_cal3 = 0.035
        cf_cal4 = 0.029
        calories_walking = (cf_cal3 * self.weight
                            + (self.get_mean_speed()**2 // self.height)
                            * cf_cal4 * self.weight) * self.duration
        return calories_walking


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    cf_cal5 = 1.1
    cf_cal6 = 2

    def __init__(self, action: int, duration: float, weight: float,
                 lenght_pool: float, count_pool: float) -> float:
        super().__init__(action, duration, weight)
        self.lenght_pool = lenght_pool
        self.count_pool = count_pool

    def get_mean_speed_swimming(self) -> float:
        speed = (self.lenght_pool) * self.count_pool / Training.M_IN_KM / self.duration
        return speed

    def get_spent_calories_swimming(self) -> float:
        calories_swimming = (self.speed
                             + Swimming.cf_cal5) * Swimming.cf_cal6 * self.weight
        return calories_swimming

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * Swimming.LEN_STEP / Training.M_IN_KM
        return distance


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type == 'SWM':
        return Swimming(*data)
    if workout_type == 'RUN':
        return Running(*data)
    if workout_type == 'WLK':
        return SportsWalking(*data)


def main(training: Training):
    """Главная функция."""
    return (InfoMessage.get_message(training.show_training_info()))


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]
    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
