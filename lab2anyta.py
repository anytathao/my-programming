# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    g=9.8 # Acceleration due to gravity in m/s^2
    height=h0 - 0.5 * g * t**2
    return round(height) # Round to one decimal place or precision

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    speed = 20 # Speed of the car in meters per second
    distance = speed * t
    return distance

if __name__ == '__main__':
    print(calculate_height(50, 3)) # 50 - 0.5 * 9.8 * 3^2 = 5.9 meters
    print(calculate_car_distance(1)) # 20 * 1= 20 meters
    print(calculate_car_distance(3)) # 20 * 3= 60 meters
