from . import DroneStabilizer

def main():
    stabilizer = DroneStabilizer()

    # Пример входных данных (данные с гироскопа и акселерометра)
    gyro_data = {'roll_rate': 0.1, 'pitch_rate': -0.1}  # Скорости изменения углов
    accel_data = {'x': 0.02, 'y': 0.01, 'z': 1.0}       # Ускорения в осях

    # Получаем команды для двигателей
    motor_commands = stabilizer.compute_commands(gyro_data, accel_data)

    # Вывод результатов
    print("Команды для двигателей:")
    for motor, value in motor_commands.items():
        print(f"{motor}: {value:.2f}")


if __name__ == "__main__":
    main()