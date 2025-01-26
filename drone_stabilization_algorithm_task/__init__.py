import numpy as np

class DroneStabilizer:
    def __init__(self):
        # Константы для P-регулятора
        self.kp_roll = 1.0  # коэффициент пропорциональности для наклона
        self.kp_pitch = 1.0  # коэффициент пропорциональности для тангажа

    def compute_commands(self, gyro_data, accel_data):
        """
        Рассчитать команды для двигателей дрона на основе данных гироскопа и акселерометра.

        :param gyro_data: Словарь с данными гироскопа {'roll_rate': x, 'pitch_rate': y}
        :param accel_data: Словарь с данными акселерометра {'x': ax, 'y': ay, 'z': az}
        :return: Словарь с командами для двигателей {'motor1': v1, 'motor2': v2, 'motor3': v3, 'motor4': v4}
        """
        # Рассчитываем отклонение от горизонтали по акселерометру
        roll_angle = np.arctan2(accel_data['y'], accel_data['z']) * (180 / np.pi)  # Углы в градусах
        pitch_angle = np.arctan2(accel_data['x'], accel_data['z']) * (180 / np.pi)

        # Рассчитываем коррекцию по P-регулятору
        roll_correction = -self.kp_roll * roll_angle
        pitch_correction = -self.kp_pitch * pitch_angle

        # Команды для двигателей (упрощённая модель квадрокоптера)
        motor1 = 1000 + roll_correction + pitch_correction
        motor2 = 1000 - roll_correction + pitch_correction
        motor3 = 1000 + roll_correction - pitch_correction
        motor4 = 1000 - roll_correction - pitch_correction

        # Ограничиваем значения двигателей
        motor1 = np.clip(motor1, 900, 1100)
        motor2 = np.clip(motor2, 900, 1100)
        motor3 = np.clip(motor3, 900, 1100)
        motor4 = np.clip(motor4, 900, 1100)

        return {
            'motor1': motor1,
            'motor2': motor2,
            'motor3': motor3,
            'motor4': motor4
        }
