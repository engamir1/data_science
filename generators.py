import random


def temperature_sensor():
    while True:
        yield random.uniform(20, 30)  # Simulate temperature readings


# use next(function ) to get next value.
print(next(temperature_sensor()))
print(temperature_sensor)

# Simulate reading from the sensor
# sensor = temperature_sensor()
# for _ in range(5):  # Print 5 readings
#     print(f"Temperature: {next(sensor):.2f}°C")
